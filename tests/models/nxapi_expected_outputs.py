NXAPI_SHOW_MODULE_OUTPUT = {
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

NXAPI_SHOW_VERSION_OUTPUT = {
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