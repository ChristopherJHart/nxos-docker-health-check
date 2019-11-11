import requests
import urllib3
import json


class NXAPI:
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        self.base_url = f"https://{self.ip}/"
        self.url = f"{self.base_url}ins"
        self.model = None
        self.modules = []
        self.nxos_version = None
        self.hw_diags_passed = None
        self.interfaces = {}
        self.copp_counters = {}
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def _send_request(self, payload):
        headers = {
            "content-type": "application/json",
        }
        try:
            response = requests.post(
                self.url,
                data=json.dumps(payload),
                headers=headers,
                auth=(self.username, self.password),
                verify=False,
            )
        except requests.exceptions.ConnectionError as exc:
            if "Connection refused" in str(exc):
                raise self.ConnectionRefused(
                    "Could not connect to NX-API for device {}! Verify that `feature nxapi` is configured on device".format(
                        self.ip
                    )
                )
        response.raise_for_status()
        return response.json()

    def _format_show_command_payload(self, cmd):
        payload = {
            "ins_api": {
                "version": "1.0",
                "type": "cli_show",
                "chunk": "0",
                "sid": "1",
                "input": cmd,
                "output_format": "json",
            }
        }
        return payload

    def _verify_successful_nxapi_output(self, json_output):
        cmd_code = json_output["ins_api"]["outputs"]["output"]["code"]
        if cmd_code == "200":
            return True
        else:
            return False

    def _get_model_from_json(self, json_output):
        if self._verify_successful_nxapi_output(json_output):
            mod_info = json_output["ins_api"]["outputs"]["output"]["body"][
                "TABLE_modinfo"
            ]["ROW_modinfo"]
            # End of Row (Nexus 9500) platforms return ROW_modinfo output as a list. Top of Rack
            # (Nexus 9200, 9300, etc.) platforms return ROW_modinfo output as a dictionary. We must
            # be able to handle both scenarios.
            if isinstance(mod_info, list):
                # If platform is EoR...
                self.modules = mod_info
                self.model = "N9K-C9500"
                # As a future enhancement, we could potentially identify the exact model (9504, 9508, etc.)
                # of the device by analyzing the strings of fabric modules. For now, we'll settle for defining
                # the general platform.
            elif isinstance(mod_info, dict):
                # If platform is ToR...
                self.model = mod_info["model"]
                self.modules.append(mod_info)

    def _get_nxos_version_from_json(self, json_output):
        if self._verify_successful_nxapi_output(json_output):
            mod_info = json_output["ins_api"]["outputs"]["output"]["body"][
                "TABLE_modwwninfo"
            ]["ROW_modwwninfo"]
            # End of Row (Nexus 9500) platforms return ROW_modwwninfo output as a list. Top of Rack
            # (Nexus 9200, 9300, etc.) platforms return ROW_modwwwninfo output as a dictionary. We must
            # be able to handle both scenarios.
            if isinstance(mod_info, list):
                # If platform is EoR...
                for module in mod_info:
                    if "SUP" in module["slottype"]:
                        self.nxos_version = module["sw"]
                        break
            elif isinstance(mod_info, dict):
                # If platform is ToR...
                self.nxos_version = mod_info["sw"]

    def _get_module_diagnostic_status_from_json(self, json_output):
        if self._verify_successful_nxapi_output(json_output):
            mod_diag_info = json_output["ins_api"]["outputs"]["output"]["body"][
                "TABLE_moddiaginfo"
            ]["ROW_moddiaginfo"]
            # End of Row (Nexus 9500) platforms return ROW_modwwninfo output as a list. Top of Rack
            # (Nexus 9200, 9300, etc.) platforms return ROW_modwwwninfo output as a dictionary. We must
            # be able to handle both scenarios.
            if isinstance(mod_diag_info, list):
                # If platform is EoR...
                for module in mod_diag_info:
                    if not "Pass" in module["diagstatus"]:
                        self.hw_diags_passed = False
                        break
                else:
                    self.hw_diags_passed = True
            elif isinstance(mod_diag_info, dict):
                # If platform is ToR...
                if "Pass" in mod_diag_info["diagstatus"]:
                    self.hw_diags_passed = True
                else:
                    self.hw_diags_passed = False

    def send_show_command(self, command):
        payload = self._format_show_command_payload(command)
        return self._send_request(payload)

    def check_device_modules(self):
        sh_mod = self.send_show_command("show module")
        self._get_model_from_json(sh_mod)
        self._get_nxos_version_from_json(sh_mod)
        self._get_module_diagnostic_status_from_json(sh_mod)

    def check_device_error_counters(self):
        interface_data = {}
        # To get accurate information, we need to get both error counters as well as normal counters for each interface.
        # To optimize further analysis, we'll segregate the two types of counters into two separate dictionaries.
        # First, let's get normal counters and populate our interface data
        counts = self.send_show_command("show interface counters")
        # These are split in two groups - RX, and TX. Let's start with RX
        returned_rx_count_info = counts["ins_api"]["outputs"]["output"]["body"][
            "TABLE_rx_counters"
        ]["ROW_rx_counters"]
        # This data looks like this:
        # [
        #   {
        #     "interface_rx": "Ethernet1/1",
        #     "eth_inbytes": 239390039,
        #     "eth_inucast": 72954
        #   },
        #   {
        #     "interface_rx": "Ethernet1/2",
        #     "eth_inbytes": 249994,
        #     "eth_inucast": 0
        #   },
        # ]
        rx_intf_names = [intf["interface_rx"] for intf in returned_rx_count_info]
        for intf in rx_intf_names:
            interface_data[intf] = {
                "errors": {},
                "normal": {},
            }
        for intf_data in returned_rx_count_info:
            for key, value in intf_data.items():
                if "interface_rx" in key:
                    # Remove redundant interface name information
                    continue
                interface_data[intf_data["interface_rx"]]["normal"][key] = value

        # Now, let's do TX
        returned_tx_count_info = counts["ins_api"]["outputs"]["output"]["body"][
            "TABLE_tx_counters"
        ]["ROW_tx_counters"]
        # This data looks like this:
        # [
        #   {
        #     "interface_tx": "Ethernet1/1",
        #     "eth_outbytes": 187082262,
        #     "eth_outucast": 7619
        #   },
        #   {
        #     "interface_tx": "Ethernet1/2",
        #     "eth_outbytes": 256555,
        #     "eth_outucast": 0
        #   },
        # ]
        for intf_data in returned_tx_count_info:
            for key, value in intf_data.items():
                if "interface_tx" in key:
                    # Remove redundant interface name information
                    continue
                interface_data[intf_data["interface_tx"]]["normal"][key] = value
        # Next, let's do error counters.
        count_errs = self.send_show_command("show interface counters errors")
        returned_err_info = count_errs["ins_api"]["outputs"]["output"]["body"][
            "TABLE_interface"
        ]["ROW_interface"]
        # This data looks like this for any single interface:
        # [
        #   {
        #     "interface": "Ethernet1/1",
        #     "eth_align_err": 0,
        #     "eth_fcs_err": 0,
        #     "eth_xmit_err": 0,
        #     "eth_rcv_err": 0,
        #     "eth_undersize": 0,
        #     "eth_outdisc": 0
        #   },
        #   {
        #     "interface": "Ethernet1/1",
        #     "eth_single_col": 0,
        #     "eth_multi_col": 0,
        #     "eth_late_col": 0,
        #     "eth_excess_col": 0,
        #     "eth_carri_sen": 0,
        #     "eth_runts": 0
        #   },
        #   {
        #     "interface": "Ethernet1/1",
        #     "eth_giants": 0,
        #     "eth_deferred_tx": 0,
        #     "eth_inmactx_err": 0,
        #     "eth_inmacrx_err": 0,
        #     "eth_symbol_err": 0
        #   },
        #   {
        #     "interface": "Ethernet1/1",
        #     "eth_indisc": 0
        #   },
        # ]
        # Populate each interface with error counter information
        for intf_data in returned_err_info:
            for key, value in intf_data.items():
                if "interface" in key:
                    # Remove redundant interface name information
                    continue
                interface_data[intf_data["interface"]]["errors"][key] = value
        # We have all the information we need!
        self.interfaces = interface_data

    def check_copp_counters(self):
        copp_counters = self.send_show_command(
            "show policy-map interface control-plane"
        )
        returned_copp_info = copp_counters["ins_api"]["outputs"]["output"]["body"][
            "TABLE_cmap"
        ]["ROW_cmap"]
        for cmap in returned_copp_info:
            cmap_name = cmap["cmap-name-out"]
            self.copp_counters[cmap_name] = {}
            slot_info = cmap["TABLE_slot"]["ROW_slot"]
            # End of Row (Nexus 9500) platforms return ROW_slot output as a list. Top of Rack
            # (Nexus 9200, 9300, etc.) platforms return ROW_slot output as a dictionary. We must
            # be able to handle both scenarios.
            if isinstance(slot_info, list):
                # If platform is EoR...
                for slot in slot_info:
                    # Diverge depending on CloudScale or First-Generation N9Ks
                    if "conform-bytes" in slot.keys():
                        self.copp_counters[cmap_name][str(slot["slot-no-out"])] = {
                            "conform_bytes": slot["conform-bytes"],
                            "violate_bytes": slot["violate-bytes"],
                        }
                    elif "conform-pkts" in slot.keys():
                        # We don't really care about packets vs. bytes here - we care about non-zero values
                        self.copp_counters[cmap_name][str(slot["slot-no-out"])] = {
                            "conform_bytes": slot["conform-pkts"],
                            "violate_bytes": slot["violate-pkts"],
                        }
            elif isinstance(slot_info, dict):
                # If platform is ToR...
                # Diverge depdning on CloudScale or First-Generation N9Ks
                if "conform-bytes" in slot_info.keys():
                    self.copp_counters[cmap_name][str(slot_info["slot-no-out"])] = {
                        "conform_bytes": slot_info["conform-bytes"],
                        "violate_bytes": slot_info["violate-bytes"],
                    }
                elif "conform-pkts" in slot_info.keys():
                    # We don't really care about packets vs. bytes here - we care about non-zero values
                    self.copp_counters[cmap_name][str(slot_info["slot-no-out"])] = {
                        "conform_bytes": slot_info["conform-pkts"],
                        "violate_bytes": slot_info["violate-pkts"],
                    }

    class ConnectionRefused(Exception):
        pass

