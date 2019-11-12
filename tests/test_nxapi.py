import pytest
import responses
import json
import logging
from nxos_health_check import nxapi
from .models import nxapi_expected_outputs

log = logging.getLogger(__name__)


class TestNxapiInit:
    def test_basic_init(self):
        example_ip = "127.0.0.1"
        example_username = "username"
        example_password = "password"
        example_base_url = "https://127.0.0.1/"
        example_url = "https://127.0.0.1/ins"
        nxapi_conn = nxapi.NXAPI(example_ip, example_username, example_password)
        assert nxapi_conn is not None
        assert nxapi_conn.ip == example_ip
        assert nxapi_conn.username == example_username
        assert nxapi_conn.password == example_password
        assert nxapi_conn.base_url == example_base_url
        assert nxapi_conn.url == example_url

    def test_another_basic_init(self):
        example_ip = "192.0.2.1"
        example_username = "another_username"
        example_password = "another_password"
        example_base_url = "https://192.0.2.1/"
        example_url = "https://192.0.2.1/ins"
        nxapi_conn = nxapi.NXAPI(example_ip, example_username, example_password)
        assert nxapi_conn is not None
        assert nxapi_conn.ip == example_ip
        assert nxapi_conn.username == example_username
        assert nxapi_conn.password == example_password
        assert nxapi_conn.base_url == example_base_url
        assert nxapi_conn.url == example_url


class TestNxapiPayload:
    def test_module_command(self):
        example_command = "show module"
        expected_payload = {
            "ins_api": {
                "version": "1.0",
                "type": "cli_show",
                "chunk": "0",
                "sid": "1",
                "input": "show module",
                "output_format": "json",
            }
        }
        example_ip = "192.0.2.1"
        example_username = "another_username"
        example_password = "another_password"

        nxapi_conn = nxapi.NXAPI(example_ip, example_username, example_password)
        returned_payload = nxapi_conn._format_show_command_payload(example_command)
        assert returned_payload == expected_payload

    def test_version_command(self):
        example_command = "show version"
        expected_payload = {
            "ins_api": {
                "version": "1.0",
                "type": "cli_show",
                "chunk": "0",
                "sid": "1",
                "input": "show version",
                "output_format": "json",
            }
        }
        example_ip = "192.0.2.1"
        example_username = "another_username"
        example_password = "another_password"

        nxapi_conn = nxapi.NXAPI(example_ip, example_username, example_password)
        returned_payload = nxapi_conn._format_show_command_payload(example_command)
        assert returned_payload == expected_payload


class TestNxapiShowCommands:
    @responses.activate
    def test_raw_module_tor_command(self):
        resp_json = nxapi_expected_outputs.NXAPI_SHOW_MODULE_TOR_OUTPUT
        responses.add(
            responses.POST, "https://127.0.0.1/ins", json=resp_json, status=200,
        )
        command = "show module"
        example_ip = "127.0.0.1"
        example_username = "username"
        example_password = "password"

        nxapi_conn = nxapi.NXAPI(example_ip, example_username, example_password)
        output = nxapi_conn.send_show_command(command)
        assert output is not None
        assert output == resp_json

    @responses.activate
    def test_raw_module_eor_command(self):
        resp_json = nxapi_expected_outputs.NXAPI_SHOW_MODULE_EOR_OUTPUT
        responses.add(
            responses.POST, "https://127.0.0.1/ins", json=resp_json, status=200,
        )
        command = "show module"
        example_ip = "127.0.0.1"
        example_username = "username"
        example_password = "password"

        nxapi_conn = nxapi.NXAPI(example_ip, example_username, example_password)
        output = nxapi_conn.send_show_command(command)
        assert output is not None
        assert output == resp_json

    def test_get_model_from_json_tor(self):
        example_ip = "127.0.0.1"
        example_username = "username"
        example_password = "password"

        nxapi_conn = nxapi.NXAPI(example_ip, example_username, example_password)
        nxapi_conn._get_model_from_json(
            nxapi_expected_outputs.NXAPI_SHOW_MODULE_TOR_OUTPUT
        )

        assert nxapi_conn.model == "N9K-C93180YC-FX"
        assert nxapi_conn.modules == [
            nxapi_expected_outputs.NXAPI_SHOW_MODULE_TOR_OUTPUT["ins_api"]["outputs"][
                "output"
            ]["body"]["TABLE_modinfo"]["ROW_modinfo"]
        ]

    def test_get_model_from_json_eor(self):
        example_ip = "127.0.0.1"
        example_username = "username"
        example_password = "password"

        nxapi_conn = nxapi.NXAPI(example_ip, example_username, example_password)
        nxapi_conn._get_model_from_json(
            nxapi_expected_outputs.NXAPI_SHOW_MODULE_EOR_OUTPUT
        )

        assert nxapi_conn.model == "N9K-C9500"
        assert (
            nxapi_conn.modules
            == nxapi_expected_outputs.NXAPI_SHOW_MODULE_EOR_OUTPUT["ins_api"][
                "outputs"
            ]["output"]["body"]["TABLE_modinfo"]["ROW_modinfo"]
        )

    @responses.activate
    def test_version_command(self):
        resp_json = nxapi_expected_outputs.NXAPI_SHOW_VERSION_OUTPUT
        responses.add(
            responses.POST, "https://127.0.0.1/ins", json=resp_json, status=200,
        )
        command = "show version"
        example_ip = "127.0.0.1"
        example_username = "username"
        example_password = "password"

        nxapi_conn = nxapi.NXAPI(example_ip, example_username, example_password)
        output = nxapi_conn.send_show_command(command)
        assert output is not None
        assert output == resp_json

    def test_get_version_from_json_tor(self):
        example_ip = "127.0.0.1"
        example_username = "username"
        example_password = "password"

        nxapi_conn = nxapi.NXAPI(example_ip, example_username, example_password)
        nxapi_conn._get_nxos_version_from_json(
            nxapi_expected_outputs.NXAPI_SHOW_MODULE_TOR_OUTPUT
        )

        assert nxapi_conn.nxos_version == "9.3(1)"

    def test_get_version_from_json_eor(self):
        example_ip = "127.0.0.1"
        example_username = "username"
        example_password = "password"

        nxapi_conn = nxapi.NXAPI(example_ip, example_username, example_password)
        nxapi_conn._get_nxos_version_from_json(
            nxapi_expected_outputs.NXAPI_SHOW_MODULE_EOR_OUTPUT
        )

        assert nxapi_conn.nxos_version == "7.0(3)I7(5a)"

    @responses.activate
    def test_check_interface_counters(self):
        def nxapi_callback(request):
            payload = json.loads(request.body)
            if payload["ins_api"]["input"] == "show interface counters":
                resp_json = nxapi_expected_outputs.NXAPI_SHOW_INTERFACE_COUNTERS
                return (
                    200,
                    {"content-type": "application/json"},
                    json.dumps(resp_json),
                )
            elif payload["ins_api"]["input"] == "show interface counters errors":
                resp_json = nxapi_expected_outputs.NXAPI_SHOW_INTERFACE_COUNTERS_ERRORS
                return (
                    200,
                    {"content-type": "application/json"},
                    json.dumps(resp_json),
                )
            else:
                return (503, {}, None)

        responses.add_callback(
            responses.POST,
            "https://127.0.0.1/ins",
            callback=nxapi_callback,
            content_type="application/json",
        )

        example_ip = "127.0.0.1"
        example_username = "username"
        example_password = "password"

        nxapi_conn = nxapi.NXAPI(example_ip, example_username, example_password)
        nxapi_conn.check_device_error_counters()

        intfs = nxapi_conn.interfaces
        assert len(intfs.keys()) == 3
        assert "mgmt0" in intfs.keys()
        assert "Ethernet1/1" in intfs.keys()
        assert "Ethernet1/2" in intfs.keys()
        # mgmt0 counters
        assert intfs["mgmt0"]["normal"]["eth_inpkts"] == 266806619
        assert intfs["mgmt0"]["normal"]["eth_inucast"] == 1344041
        assert intfs["mgmt0"]["normal"]["eth_inmcast"] == 608813
        assert intfs["mgmt0"]["normal"]["eth_inbcast"] == 133992
        assert intfs["mgmt0"]["normal"]["eth_outpkts"] == 331850552
        assert intfs["mgmt0"]["normal"]["eth_outucast"] == 1308143
        assert intfs["mgmt0"]["normal"]["eth_outmcast"] == 0
        assert intfs["mgmt0"]["normal"]["eth_outbcast"] == 31
        assert intfs["mgmt0"]["errors"]["eth_align_err"] == 0
        assert intfs["mgmt0"]["errors"]["eth_fcs_err"] == 0
        assert intfs["mgmt0"]["errors"]["eth_single_col"] == 0
        assert intfs["mgmt0"]["errors"]["eth_multi_col"] == 0
        assert intfs["mgmt0"]["errors"]["eth_late_col"] == 0
        assert intfs["mgmt0"]["errors"]["eth_excess_col"] == 0
        assert intfs["mgmt0"]["errors"]["eth_giants"] == 0
        assert intfs["mgmt0"]["errors"]["eth_sqetest_err"] == 0
        assert intfs["mgmt0"]["errors"]["eth_deferred_tx"] == 0
        assert intfs["mgmt0"]["errors"]["eth_inmactx_err"] == 0
        assert intfs["mgmt0"]["errors"]["eth_inmacrx_err"] == 0
        assert intfs["mgmt0"]["errors"]["eth_symbol_err"] == 0
        # Eth1/1 counters
        log.warning(intfs["Ethernet1/1"]["normal"])
        assert intfs["Ethernet1/1"]["normal"]["eth_inbytes"] == 288825287
        assert intfs["Ethernet1/1"]["normal"]["eth_inucast"] == 73625
        assert intfs["Ethernet1/1"]["normal"]["eth_inmcast"] == 2805707
        assert intfs["Ethernet1/1"]["normal"]["eth_inbcast"] == 3
        assert intfs["Ethernet1/1"]["normal"]["eth_outbytes"] == 225239460
        assert intfs["Ethernet1/1"]["normal"]["eth_outucast"] == 8286
        assert intfs["Ethernet1/1"]["normal"]["eth_outmcast"] == 2821973
        assert intfs["Ethernet1/1"]["normal"]["eth_outbcast"] == 2
        assert intfs["Ethernet1/1"]["errors"]["eth_align_err"] == 0
        assert intfs["Ethernet1/1"]["errors"]["eth_fcs_err"] == 0
        assert intfs["Ethernet1/1"]["errors"]["eth_xmit_err"] == 0
        assert intfs["Ethernet1/1"]["errors"]["eth_rcv_err"] == 15
        assert intfs["Ethernet1/1"]["errors"]["eth_undersize"] == 0
        assert intfs["Ethernet1/1"]["errors"]["eth_outdisc"] == 0
        assert intfs["Ethernet1/1"]["errors"]["eth_single_col"] == 0
        assert intfs["Ethernet1/1"]["errors"]["eth_multi_col"] == 0
        assert intfs["Ethernet1/1"]["errors"]["eth_late_col"] == 0
        assert intfs["Ethernet1/1"]["errors"]["eth_excess_col"] == 0
        assert intfs["Ethernet1/1"]["errors"]["eth_carri_sen"] == 0
        assert intfs["Ethernet1/1"]["errors"]["eth_runts"] == 0
        assert intfs["Ethernet1/1"]["errors"]["eth_giants"] == 15
        assert intfs["Ethernet1/1"]["errors"]["eth_deferred_tx"] == 0
        assert intfs["Ethernet1/1"]["errors"]["eth_inmactx_err"] == 0
        assert intfs["Ethernet1/1"]["errors"]["eth_inmacrx_err"] == 0
        assert intfs["Ethernet1/1"]["errors"]["eth_symbol_err"] == 0
        # Eth1/2 counters
        assert intfs["Ethernet1/2"]["normal"]["eth_inbytes"] == 1900871
        assert intfs["Ethernet1/2"]["normal"]["eth_inucast"] == 0
        assert intfs["Ethernet1/2"]["normal"]["eth_inmcast"] == 8061
        assert intfs["Ethernet1/2"]["normal"]["eth_inbcast"] == 0
        assert intfs["Ethernet1/2"]["normal"]["eth_outbytes"] == 1955299
        assert intfs["Ethernet1/2"]["normal"]["eth_outucast"] == 0
        assert intfs["Ethernet1/2"]["normal"]["eth_outmcast"] == 8870
        assert intfs["Ethernet1/2"]["normal"]["eth_outbcast"] == 0
        assert intfs["Ethernet1/2"]["errors"]["eth_align_err"] == 0
        assert intfs["Ethernet1/2"]["errors"]["eth_fcs_err"] == 0
        assert intfs["Ethernet1/2"]["errors"]["eth_xmit_err"] == 0
        assert intfs["Ethernet1/2"]["errors"]["eth_rcv_err"] == 0
        assert intfs["Ethernet1/2"]["errors"]["eth_undersize"] == 0
        assert intfs["Ethernet1/2"]["errors"]["eth_outdisc"] == 0
        assert intfs["Ethernet1/2"]["errors"]["eth_single_col"] == 0
        assert intfs["Ethernet1/2"]["errors"]["eth_multi_col"] == 0
        assert intfs["Ethernet1/2"]["errors"]["eth_late_col"] == 0
        assert intfs["Ethernet1/2"]["errors"]["eth_excess_col"] == 0
        assert intfs["Ethernet1/2"]["errors"]["eth_carri_sen"] == 0
        assert intfs["Ethernet1/2"]["errors"]["eth_runts"] == 0
        assert intfs["Ethernet1/2"]["errors"]["eth_giants"] == 0
        assert intfs["Ethernet1/2"]["errors"]["eth_deferred_tx"] == 0
        assert intfs["Ethernet1/2"]["errors"]["eth_inmactx_err"] == 0
        assert intfs["Ethernet1/2"]["errors"]["eth_inmacrx_err"] == 0
        assert intfs["Ethernet1/2"]["errors"]["eth_symbol_err"] == 0
