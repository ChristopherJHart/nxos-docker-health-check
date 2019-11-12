NXAPI_SHOW_VERSION_OUTPUT = {
    "ins_api": {
        "type": "cli_show",
        "version": "1.0",
        "sid": "eoc",
        "outputs": {
            "output": {
                "input": "show version",
                "msg": "Success",
                "code": "200",
                "body": {
                    "header_str": 'Cisco Nexus Operating System (NX-OS) Software\nTAC support: http://www.cisco.com/tac\nCopyright (C) 2002-2019, Cisco and/or its affiliates.\nAll rights reserved.\nThe copyrights to certain works contained in this software are\nowned by other third parties and used and distributed under their own\nlicenses, such as open source.  This software is provided "as is," and unless\notherwise stated, there is no warranty, express or implied, including but not\nlimited to warranties of merchantability and fitness for a particular purpose.\nCertain components of this software are licensed under\nthe GNU General Public License (GPL) version 2.0 or \nGNU General Public License (GPL) version 3.0  or the GNU\nLesser General Public License (LGPL) Version 2.1 or \nLesser General Public License (LGPL) Version 2.0. \nA copy of each such license is available at\nhttp://www.opensource.org/licenses/gpl-2.0.php and\nhttp://opensource.org/licenses/gpl-3.0.html and\nhttp://www.opensource.org/licenses/lgpl-2.1.php and\nhttp://www.gnu.org/licenses/old-licenses/library.txt.\n',
                    "bios_ver_str": "05.38",
                    "kickstart_ver_str": "9.3(1)",
                    "nxos_ver_str": "9.3(1)",
                    "bios_cmpl_time": "06/12/2019",
                    "kick_file_name": "bootflash:///nxos.9.3.1.bin",
                    "nxos_file_name": "bootflash:///nxos.9.3.1.bin",
                    "kick_cmpl_time": "7/18/2019 15:00:00",
                    "nxos_cmpl_time": "7/18/2019 15:00:00",
                    "kick_tmstmp": "07/19/2019 00:04:48",
                    "nxos_tmstmp": "07/19/2019 00:04:48",
                    "chassis_id": "Nexus9000 C93180YC-FX Chassis",
                    "cpu_name": "Intel(R) Xeon(R) CPU D-1528 @ 1.90GHz",
                    "memory": 65808228,
                    "mem_type": "kB",
                    "proc_board_id": "FDO22170SBK",
                    "host_name": "RTP-HOM-VTEP-1",
                    "bootflash_size": 115805356,
                    "kern_uptm_days": 3,
                    "kern_uptm_hrs": 1,
                    "kern_uptm_mins": 50,
                    "kern_uptm_secs": 56,
                    "rr_usecs": 263685,
                    "rr_ctime": "Wed Nov  6 00:42:22 2019",
                    "rr_reason": "Reset due to upgrade",
                    "rr_sys_ver": "7.0(3)I7(6)",
                    "rr_service": "",
                    "plugins": "Core Plugin, Ethernet Plugin",
                    "manufacturer": "Cisco Systems, Inc.",
                    "TABLE_package_list": {"ROW_package_list": {"package_id": ""}},
                },
            }
        },
    }
}

NXAPI_SHOW_MODULE_TOR_OUTPUT = {
    "ins_api": {
        "type": "cli_show",
        "version": "1.0",
        "sid": "eoc",
        "outputs": {
            "output": {
                "input": "show module",
                "msg": "Success",
                "code": "200",
                "body": {
                    "TABLE_modwwninfo": {
                        "ROW_modwwninfo": {
                            "modwwn": 1,
                            "sw": "9.3(1)",
                            "hw": "1.1",
                            "slottype": "NA",
                        }
                    },
                    "TABLE_modmacinfo": {
                        "ROW_modmacinfo": {
                            "modmac": 1,
                            "mac": " 00-de-fb-fb-50-e0 to 00-de-fb-fb-51-3f  ",
                            "serialnum": "FDO22170SBK",
                        }
                    },
                    "TABLE_modinfo": {
                        "ROW_modinfo": {
                            "modinf": 1,
                            "ports": 54,
                            "modtype": "48x10/25G/32G + 6x40/100G Ethernet/FC Module",
                            "model": "N9K-C93180YC-FX",
                            "status": "active *",
                        }
                    },
                    "TABLE_moddiaginfo": {
                        "ROW_moddiaginfo": {"mod": 1, "diagstatus": "Pass"}
                    },
                },
            }
        },
    }
}

NXAPI_SHOW_MODULE_EOR_OUTPUT = {
    "ins_api": {
        "type": "cli_show",
        "version": "1.0",
        "sid": "eoc",
        "outputs": {
            "output": {
                "input": "show module",
                "msg": "Success",
                "code": "200",
                "body": {
                    "TABLE_modwwninfo": {
                        "ROW_modwwninfo": [
                            {
                                "modwwn": 1,
                                "sw": "7.0(3)I7(5a)",
                                "hw": "1.3",
                                "slottype": "LC1",
                            },
                            {
                                "modwwn": 3,
                                "sw": "7.0(3)I7(5a)",
                                "hw": "1.4",
                                "slottype": "LC3",
                            },
                            {
                                "modwwn": 4,
                                "sw": "7.0(3)I7(5a)",
                                "hw": "2.1",
                                "slottype": "LC4",
                            },
                            {
                                "modwwn": 21,
                                "sw": "7.0(3)I7(5a)",
                                "hw": "1.2",
                                "slottype": "FM1",
                            },
                            {
                                "modwwn": 22,
                                "sw": "7.0(3)I7(5a)",
                                "hw": "1.2",
                                "slottype": "FM2",
                            },
                            {
                                "modwwn": 23,
                                "sw": "7.0(3)I7(5a)",
                                "hw": "1.2",
                                "slottype": "FM3",
                            },
                            {
                                "modwwn": 24,
                                "sw": "7.0(3)I7(5a)",
                                "hw": "1.2",
                                "slottype": "FM4",
                            },
                            {
                                "modwwn": 25,
                                "sw": "7.0(3)I7(5a)",
                                "hw": "1.2",
                                "slottype": "FM5",
                            },
                            {
                                "modwwn": 26,
                                "sw": "7.0(3)I7(5a)",
                                "hw": "1.2",
                                "slottype": "FM6",
                            },
                            {
                                "modwwn": 27,
                                "sw": "7.0(3)I7(5a)",
                                "hw": "1.5",
                                "slottype": "SUP1",
                            },
                            {
                                "modwwn": 28,
                                "sw": "7.0(3)I7(5a)",
                                "hw": "1.0",
                                "slottype": "SUP2",
                            },
                            {
                                "modwwn": 29,
                                "sw": "7.0(3)I7(5a)",
                                "hw": "1.4",
                                "slottype": "SC1",
                            },
                            {
                                "modwwn": 30,
                                "sw": "7.0(3)I7(5a)",
                                "hw": "1.4",
                                "slottype": "SC2",
                            },
                        ]
                    },
                    "TABLE_modmacinfo": {
                        "ROW_modmacinfo": [
                            {
                                "modmac": 1,
                                "mac": " 80-e0-1d-34-df-98 to 80-e0-1d-34-e0-2b  ",
                                "serialnum": "SAL1925HAEX",
                            },
                            {
                                "modmac": 3,
                                "mac": " 18-8b-9d-4d-1b-6c to 18-8b-9d-4d-1b-af  ",
                                "serialnum": "SAL1927J5EH",
                            },
                            {
                                "modmac": 4,
                                "mac": " 18-8b-9d-4c-c3-bc to 18-8b-9d-4c-c3-ff  ",
                                "serialnum": "SAL1924GNNL",
                            },
                            {"modmac": 21, "mac": " NA ", "serialnum": "SAL1926HYQY"},
                            {"modmac": 22, "mac": " NA ", "serialnum": "SAL1926HYKY"},
                            {"modmac": 23, "mac": " NA ", "serialnum": "SAL1926HPP2"},
                            {"modmac": 24, "mac": " NA ", "serialnum": "SAL1926HYJF"},
                            {"modmac": 25, "mac": " NA ", "serialnum": "SAL1926HYPV"},
                            {"modmac": 26, "mac": " NA ", "serialnum": "SAL1926HYF2"},
                            {
                                "modmac": 27,
                                "mac": " 64-f6-9d-06-b9-b8 to 64-f6-9d-06-b9-c9  ",
                                "serialnum": "SAL1922FV75",
                            },
                            {
                                "modmac": 28,
                                "mac": " c0-67-af-a0-e0-b6 to c0-67-af-a0-e0-c7  ",
                                "serialnum": "SAL1747GLRM",
                            },
                            {"modmac": 29, "mac": " NA ", "serialnum": "SAL1926J30F"},
                            {"modmac": 30, "mac": " NA ", "serialnum": "SAL1926J2X6"},
                        ]
                    },
                    "TABLE_modinfo": {
                        "ROW_modinfo": [
                            {
                                "modinf": 1,
                                "ports": 36,
                                "modtype": "36p 40G Ethernet Module",
                                "model": "N9K-X9636PQ",
                                "status": "ok",
                            },
                            {
                                "modinf": 3,
                                "ports": 52,
                                "modtype": "48x1/10G SFP+ 4x40G Ethernet Module",
                                "model": "N9K-X9564PX",
                                "status": "ok",
                            },
                            {
                                "modinf": 4,
                                "ports": 52,
                                "modtype": "48x1/10G-T 4x40G Ethernet Module",
                                "model": "N9K-X9464TX",
                                "status": "ok",
                            },
                            {
                                "modinf": 21,
                                "ports": 0,
                                "modtype": "Fabric Module",
                                "model": "N9K-C9504-FM",
                                "status": "ok",
                            },
                            {
                                "modinf": 22,
                                "ports": 0,
                                "modtype": "Fabric Module",
                                "model": "N9K-C9504-FM",
                                "status": "ok",
                            },
                            {
                                "modinf": 23,
                                "ports": 0,
                                "modtype": "Fabric Module",
                                "model": "N9K-C9504-FM",
                                "status": "ok",
                            },
                            {
                                "modinf": 24,
                                "ports": 0,
                                "modtype": "Fabric Module",
                                "model": "N9K-C9504-FM",
                                "status": "ok",
                            },
                            {
                                "modinf": 25,
                                "ports": 0,
                                "modtype": "Fabric Module",
                                "model": "N9K-C9504-FM",
                                "status": "ok",
                            },
                            {
                                "modinf": 26,
                                "ports": 0,
                                "modtype": "Fabric Module",
                                "model": "N9K-C9504-FM",
                                "status": "ok",
                            },
                            {
                                "modinf": 27,
                                "ports": 0,
                                "modtype": "Supervisor Module",
                                "model": "N9K-SUP-A",
                                "status": "active *",
                            },
                            {
                                "modinf": 28,
                                "ports": 0,
                                "modtype": "Supervisor Module",
                                "model": "N9K-SUP-A",
                                "status": "ha-standby",
                            },
                            {
                                "modinf": 29,
                                "ports": 0,
                                "modtype": "System Controller",
                                "model": "N9K-SC-A",
                                "status": "standby",
                            },
                            {
                                "modinf": 30,
                                "ports": 0,
                                "modtype": "System Controller",
                                "model": "N9K-SC-A",
                                "status": "active",
                            },
                        ]
                    },
                    "TABLE_moddiaginfo": {
                        "ROW_moddiaginfo": [
                            {"mod": 1, "diagstatus": "Pass"},
                            {"mod": 3, "diagstatus": "Pass"},
                            {"mod": 4, "diagstatus": "Pass"},
                            {"mod": 21, "diagstatus": "Pass"},
                            {"mod": 22, "diagstatus": "Pass"},
                            {"mod": 23, "diagstatus": "Pass"},
                            {"mod": 24, "diagstatus": "Pass"},
                            {"mod": 25, "diagstatus": "Pass"},
                            {"mod": 26, "diagstatus": "Pass"},
                            {"mod": 27, "diagstatus": "Pass"},
                            {"mod": 28, "diagstatus": "Pass"},
                            {"mod": 29, "diagstatus": "Pass"},
                            {"mod": 30, "diagstatus": "Pass"},
                        ]
                    },
                },
            }
        },
    }
}

NXAPI_SHOW_INTERFACE_COUNTERS = {
    "ins_api": {
        "type": "cli_show",
        "version": "1.0",
        "sid": "eoc",
        "outputs": {
            "output": {
                "input": "show interface counters",
                "msg": "Success",
                "code": "200",
                "body": {
                    "TABLE_rx_counters": {
                        "ROW_rx_counters": [
                            {
                                "interface_rx": "mgmt0",
                                "eth_inpkts": 266806619,
                                "eth_inucast": 1344041,
                            },
                            {
                                "interface_rx": "Ethernet1/1",
                                "eth_inbytes": 288825287,
                                "eth_inucast": 73625,
                            },
                            {
                                "interface_rx": "Ethernet1/2",
                                "eth_inbytes": 1900871,
                                "eth_inucast": 0,
                            },
                            {
                                "interface_rx": "mgmt0",
                                "eth_inmcast": 608813,
                                "eth_inbcast": 133992,
                            },
                            {
                                "interface_rx": "Ethernet1/1",
                                "eth_inmcast": 2805707,
                                "eth_inbcast": 3,
                            },
                            {
                                "interface_rx": "Ethernet1/2",
                                "eth_inmcast": 8061,
                                "eth_inbcast": 0,
                            },
                        ]
                    },
                    "TABLE_tx_counters": {
                        "ROW_tx_counters": [
                            {
                                "interface_tx": "mgmt0",
                                "eth_outpkts": 331850552,
                                "eth_outucast": 1308143,
                            },
                            {
                                "interface_tx": "Ethernet1/1",
                                "eth_outbytes": 225239460,
                                "eth_outucast": 8286,
                            },
                            {
                                "interface_tx": "Ethernet1/2",
                                "eth_outbytes": 1955299,
                                "eth_outucast": 0,
                            },
                            {
                                "interface_tx": "mgmt0",
                                "eth_outmcast": 0,
                                "eth_outbcast": 31,
                            },
                            {
                                "interface_tx": "Ethernet1/1",
                                "eth_outmcast": 2821973,
                                "eth_outbcast": 2,
                            },
                            {
                                "interface_tx": "Ethernet1/2",
                                "eth_outmcast": 8870,
                                "eth_outbcast": 0,
                            },
                        ]
                    },
                },
            }
        },
    }
}

NXAPI_SHOW_INTERFACE_COUNTERS_ERRORS = {
    "ins_api": {
        "type": "cli_show",
        "version": "1.0",
        "sid": "eoc",
        "outputs": {
            "output": {
                "input": "show interface counters errors",
                "msg": "Success",
                "code": "200",
                "body": {
                    "TABLE_interface": {
                        "ROW_interface": [
                            {
                                "interface": "mgmt0",
                                "eth_align_err": 0,
                                "eth_fcs_err": 0,
                            },
                            {
                                "interface": "Ethernet1/1",
                                "eth_align_err": 0,
                                "eth_fcs_err": 0,
                                "eth_xmit_err": 0,
                                "eth_rcv_err": 15,
                                "eth_undersize": 0,
                                "eth_outdisc": 0,
                            },
                            {
                                "interface": "Ethernet1/2",
                                "eth_align_err": 0,
                                "eth_fcs_err": 0,
                                "eth_xmit_err": 0,
                                "eth_rcv_err": 0,
                                "eth_undersize": 0,
                                "eth_outdisc": 0,
                            },
                            {
                                "interface": "mgmt0",
                                "eth_single_col": 0,
                                "eth_multi_col": 0,
                                "eth_late_col": 0,
                                "eth_excess_col": 0,
                            },
                            {
                                "interface": "Ethernet1/1",
                                "eth_single_col": 0,
                                "eth_multi_col": 0,
                                "eth_late_col": 0,
                                "eth_excess_col": 0,
                                "eth_carri_sen": 0,
                                "eth_runts": 0,
                            },
                            {
                                "interface": "Ethernet1/2",
                                "eth_single_col": 0,
                                "eth_multi_col": 0,
                                "eth_late_col": 0,
                                "eth_excess_col": 0,
                                "eth_carri_sen": 0,
                                "eth_runts": 0,
                            },
                            {
                                "interface": "mgmt0",
                                "eth_giants": 0,
                                "eth_sqetest_err": 0,
                                "eth_deferred_tx": 0,
                                "eth_inmactx_err": 0,
                                "eth_inmacrx_err": 0,
                                "eth_symbol_err": 0,
                            },
                            {
                                "interface": "Ethernet1/1",
                                "eth_giants": 15,
                                "eth_deferred_tx": 0,
                                "eth_inmactx_err": 0,
                                "eth_inmacrx_err": 0,
                                "eth_symbol_err": 0,
                            },
                            {
                                "interface": "Ethernet1/2",
                                "eth_giants": 0,
                                "eth_deferred_tx": 0,
                                "eth_inmactx_err": 0,
                                "eth_inmacrx_err": 0,
                                "eth_symbol_err": 0,
                            },
                        ]
                    }
                },
            }
        },
    }
}

NXAPI_SHOW_COPP_COUNTERS_TOR = {
    "ins_api": {
        "type": "cli_show",
        "version": "1.0",
        "sid": "eoc",
        "outputs": {
            "output": {
                "input": "show policy-map interface control-plane",
                "msg": "Success",
                "code": "200",
                "body": {
                    "pmap-name": "copp-system-p-policy-strict",
                    "TABLE_cmap": {
                        "ROW_cmap": [
                            {
                                "cmap-key": "copp-system-p-class-l3uc-data",
                                "cmap-name-out": "copp-system-p-class-l3uc-data",
                                "opt_any_or_all": "match-any",
                                "set_vld_flg": 1,
                                "cir": "800",
                                "opt_kbps_mbps_gbps_pps_cir": "kbps",
                                "bc": "32000",
                                "opt_kbytes_mbytes_gbytes_bc": "bytes",
                                "TABLE_slot": {
                                    "ROW_slot": {
                                        "slot-no-out": 1,
                                        "conform-bytes": "0",
                                        "opt_drop_transmit_conform": "transmit",
                                        "violate-bytes": "0",
                                        "opt_drop_transmit_violate": "drop",
                                    }
                                },
                                "cos": {"cos-val": 1},
                                "TABLE_match": {
                                    "ROW_match": {
                                        "match-key": 1,
                                        "exception": {"opt_match_excpt": "glean"},
                                    }
                                },
                            },
                            {
                                "cmap-key": "copp-system-p-class-critical",
                                "cmap-name-out": "copp-system-p-class-critical",
                                "opt_any_or_all": "match-any",
                                "set_vld_flg": 1,
                                "cir": "36000",
                                "opt_kbps_mbps_gbps_pps_cir": "kbps",
                                "bc": "1280000",
                                "opt_kbytes_mbytes_gbytes_bc": "bytes",
                                "TABLE_slot": {
                                    "ROW_slot": {
                                        "slot-no-out": 1,
                                        "conform-bytes": "29434960",
                                        "opt_drop_transmit_conform": "transmit",
                                        "violate-bytes": "0",
                                        "opt_drop_transmit_violate": "drop",
                                    }
                                },
                                "cos": {"cos-val": 7},
                                "TABLE_match": {
                                    "ROW_match": [
                                        {
                                            "match-key": 1,
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-bgp"
                                            },
                                        },
                                        {
                                            "match-key": 2,
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-rip"
                                            },
                                        },
                                        {
                                            "match-key": 3,
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-vpc"
                                            },
                                        },
                                        {
                                            "match-key": 4,
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-bgp6"
                                            },
                                        },
                                        {
                                            "match-key": 5,
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-ospf"
                                            },
                                        },
                                        {
                                            "match-key": 6,
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-rip6"
                                            },
                                        },
                                        {
                                            "match-key": 7,
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-eigrp"
                                            },
                                        },
                                        {
                                            "match-key": 8,
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-ospf6"
                                            },
                                        },
                                        {
                                            "match-key": 9,
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-eigrp6"
                                            },
                                        },
                                        {
                                            "match-key": 10,
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-auto-rp"
                                            },
                                        },
                                        {
                                            "match-key": 11,
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-mac-l3-isis"
                                            },
                                        },
                                    ]
                                },
                            },
                        ]
                    },
                },
            }
        },
    }
}

NXAPI_SHOW_COPP_COUNTERS_EOR = {
    "ins_api": {
        "type": "cli_show",
        "version": "1.0",
        "sid": "eoc",
        "outputs": {
            "output": {
                "input": "show policy-map interface control-plane",
                "msg": "Success",
                "code": "200",
                "body": {
                    "pmap-name": "copp-system-p-policy-strict",
                    "TABLE_cmap": {
                        "ROW_cmap": [
                            {
                                "cmap-key": "copp-system-p-class-l3uc-data",
                                "cmap-name-out": "copp-system-p-class-l3uc-data",
                                "opt_any_or_all": "match-any",
                                "set_vld_flg": "1",
                                "cir": "250",
                                "opt_kbps_mbps_gbps_pps_cir": "pps",
                                "bc": "32",
                                "opt_kbytes_mbytes_gbytes_bc": "packets",
                                "TABLE_slot": {
                                    "ROW_slot": [
                                        {
                                            "slot-no-out": "1",
                                            "conform-pkts": "0",
                                            "opt_drop_transmit_conform": "transmit",
                                            "violate-pkts": "0",
                                            "opt_drop_transmit_violate": "drop",
                                        },
                                        {
                                            "slot-no-out": "3",
                                            "conform-pkts": "0",
                                            "opt_drop_transmit_conform": "transmit",
                                            "violate-pkts": "0",
                                            "opt_drop_transmit_violate": "drop",
                                        },
                                        {
                                            "slot-no-out": "4",
                                            "conform-pkts": "0",
                                            "opt_drop_transmit_conform": "transmit",
                                            "violate-pkts": "0",
                                            "opt_drop_transmit_violate": "drop",
                                        },
                                        {
                                            "slot-no-out": "21",
                                            "conform-pkts": "0",
                                            "opt_drop_transmit_conform": "transmit",
                                            "violate-pkts": "0",
                                            "opt_drop_transmit_violate": "drop",
                                        },
                                        {
                                            "slot-no-out": "22",
                                            "conform-pkts": "0",
                                            "opt_drop_transmit_conform": "transmit",
                                            "violate-pkts": "0",
                                            "opt_drop_transmit_violate": "drop",
                                        },
                                        {
                                            "slot-no-out": "23",
                                            "conform-pkts": "0",
                                            "opt_drop_transmit_conform": "transmit",
                                            "violate-pkts": "0",
                                            "opt_drop_transmit_violate": "drop",
                                        },
                                        {
                                            "slot-no-out": "24",
                                            "conform-pkts": "0",
                                            "opt_drop_transmit_conform": "transmit",
                                            "violate-pkts": "0",
                                            "opt_drop_transmit_violate": "drop",
                                        },
                                        {
                                            "slot-no-out": "25",
                                            "conform-pkts": "0",
                                            "opt_drop_transmit_conform": "transmit",
                                            "violate-pkts": "0",
                                            "opt_drop_transmit_violate": "drop",
                                        },
                                        {
                                            "slot-no-out": "26",
                                            "conform-pkts": "0",
                                            "opt_drop_transmit_conform": "transmit",
                                            "violate-pkts": "0",
                                            "opt_drop_transmit_violate": "drop",
                                        },
                                    ]
                                },
                                "cos": {"cos-val": "1"},
                                "TABLE_match": {
                                    "ROW_match": {
                                        "match-key": "1",
                                        "exception": {"opt_match_excpt": "glean"},
                                    }
                                },
                            },
                            {
                                "cmap-key": "copp-system-p-class-critical",
                                "cmap-name-out": "copp-system-p-class-critical",
                                "opt_any_or_all": "match-any",
                                "set_vld_flg": "1",
                                "cir": "19000",
                                "opt_kbps_mbps_gbps_pps_cir": "pps",
                                "bc": "128",
                                "opt_kbytes_mbytes_gbytes_bc": "packets",
                                "TABLE_slot": {
                                    "ROW_slot": [
                                        {
                                            "slot-no-out": "1",
                                            "conform-pkts": "2206859",
                                            "opt_drop_transmit_conform": "transmit",
                                            "violate-pkts": "0",
                                            "opt_drop_transmit_violate": "drop",
                                        },
                                        {
                                            "slot-no-out": "3",
                                            "conform-pkts": "0",
                                            "opt_drop_transmit_conform": "transmit",
                                            "violate-pkts": "0",
                                            "opt_drop_transmit_violate": "drop",
                                        },
                                        {
                                            "slot-no-out": "4",
                                            "conform-pkts": "0",
                                            "opt_drop_transmit_conform": "transmit",
                                            "violate-pkts": "0",
                                            "opt_drop_transmit_violate": "drop",
                                        },
                                        {
                                            "slot-no-out": "21",
                                            "conform-pkts": "0",
                                            "opt_drop_transmit_conform": "transmit",
                                            "violate-pkts": "0",
                                            "opt_drop_transmit_violate": "drop",
                                        },
                                        {
                                            "slot-no-out": "22",
                                            "conform-pkts": "2206857",
                                            "opt_drop_transmit_conform": "transmit",
                                            "violate-pkts": "0",
                                            "opt_drop_transmit_violate": "drop",
                                        },
                                        {
                                            "slot-no-out": "23",
                                            "conform-pkts": "0",
                                            "opt_drop_transmit_conform": "transmit",
                                            "violate-pkts": "0",
                                            "opt_drop_transmit_violate": "drop",
                                        },
                                        {
                                            "slot-no-out": "24",
                                            "conform-pkts": "0",
                                            "opt_drop_transmit_conform": "transmit",
                                            "violate-pkts": "0",
                                            "opt_drop_transmit_violate": "drop",
                                        },
                                        {
                                            "slot-no-out": "25",
                                            "conform-pkts": "0",
                                            "opt_drop_transmit_conform": "transmit",
                                            "violate-pkts": "0",
                                            "opt_drop_transmit_violate": "drop",
                                        },
                                        {
                                            "slot-no-out": "26",
                                            "conform-pkts": "0",
                                            "opt_drop_transmit_conform": "transmit",
                                            "violate-pkts": "0",
                                            "opt_drop_transmit_violate": "drop",
                                        },
                                    ]
                                },
                                "cos": {"cos-val": "7"},
                                "TABLE_match": {
                                    "ROW_match": [
                                        {
                                            "match-key": "1",
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-bgp"
                                            },
                                        },
                                        {
                                            "match-key": "2",
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-rip"
                                            },
                                        },
                                        {
                                            "match-key": "3",
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-vpc"
                                            },
                                        },
                                        {
                                            "match-key": "4",
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-bgp6"
                                            },
                                        },
                                        {
                                            "match-key": "5",
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-ospf"
                                            },
                                        },
                                        {
                                            "match-key": "6",
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-rip6"
                                            },
                                        },
                                        {
                                            "match-key": "7",
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-eigrp"
                                            },
                                        },
                                        {
                                            "match-key": "8",
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-ospf6"
                                            },
                                        },
                                        {
                                            "match-key": "9",
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-eigrp6"
                                            },
                                        },
                                        {
                                            "match-key": "10",
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-auto-rp"
                                            },
                                        },
                                        {
                                            "match-key": "11",
                                            "access_grp": {
                                                "acc_grp_name": "copp-system-p-acl-mac-l3-isis"
                                            },
                                        },
                                    ]
                                },
                            },
                        ]
                    },
                },
            }
        },
    }
}
