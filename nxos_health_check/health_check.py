import sys
import os
import configparser
import logging
import logging.config
import requests
from pprint import pformat
from nxapi import NXAPI


__author__ = "Christopher Hart, Yogesh Ramdoss"
__maintainer__ = "Christopher Hart"
__email__ = "chart2@cisco.com"
__copyright__ = "Copyright (c) 2019 Cisco Systems. All rights reserved."
__credits__ = ["Christopher Hart", "Yogesh Ramdoss"]
__license__ = """
################################################################################
# Copyright (c) 2019 Cisco and/or its affiliates.
# 
# This software is licensed to you under the terms of the Cisco Sample
# Code License, Version 1.1 (the "License"). You may obtain a copy of the
# License at
# 
#                https://developer.cisco.com/docs/licenses
# 
# All use of the material herein must be in accordance with the terms of
# the License. All rights not expressly granted by the License are
# reserved. Unless required by applicable law or agreed to separately in
# writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.
################################################################################
"""

CFG_FILENAME = os.getenv("CFG_FILENAME", "/app/config.ini")
DEBUG = os.getenv("DEBUG")


def main():
    log.info("[INIT] Initializing health check")
    devices = []
    credentials = {"username": None, "password": None}
    log.info("[CFG] Analyzing configuration...")
    analyze_configuration(devices, credentials)
    log.info("[HLTH] Performing health check on %s devices", len(devices))
    for device in devices:
        nxapi_conn = NXAPI(
            device["ip"], credentials["username"], credentials["password"]
        )
        # Verifies:
        # - Device model/modules
        # - Device NX-OS software release
        # - Device module diagnostic tests have passed
        nxapi_conn.check_device_modules()
        log.info(
            "[DEV] Device with IP %s is a %s running NX-OS %s",
            nxapi_conn.ip,
            nxapi_conn.model,
            nxapi_conn.nxos_version,
        )
        if nxapi_conn.hw_diags_passed:
            log.info("[DEV] \tDiagnostics passing: %s", nxapi_conn.hw_diags_passed)
        elif not nxapi_conn.hw_diags_passed:
            log.error("[DEV] \tDiagnostics passing: %s", nxapi_conn.hw_diags_passed)
        nxapi_conn.check_device_error_counters()
        report_interfaces(nxapi_conn.interfaces)
        nxapi_conn.check_copp_counters()
        report_copp_counters(nxapi_conn.copp_counters)
        nxapi_conn.check_intf_status()
        report_intf_status(nxapi_conn.interfaces)

def analyze_configuration(devices, credentials, filename=CFG_FILENAME):
    config = configparser.ConfigParser()
    with open(CFG_FILENAME) as openfile:
        config.read_string(openfile.read())
    for device_name, ip in config["Devices"].items():
        devices.append({"name": device_name, "ip": ip})
    credentials["username"] = config["Credentials"]["username"]
    credentials["password"] = config["Credentials"]["password"]

def report_interfaces(interfaces):
    issue_found = False
    for interface in interfaces.keys():
        for counter_name in interfaces[interface]["errors"].keys():
            cnt = interfaces[interface]["errors"][counter_name]
            if cnt != 0:
                issue_found = True
                log.error(
                    "[DEV] \tInterface %s error counter %s: %s",
                    interface,
                    counter_name,
                    cnt,
                )
    if not issue_found:
        log.info("[DEV] \tNo non-zero interface error counters")

def report_copp_counters(counters):
    issue_found = False
    for cmap in counters.keys():
        for module in counters[cmap].keys():
            violations = int(counters[cmap][module]["violate_bytes"])
            if violations != 0:
                issue_found = True
                log.error(
                    "[DEV] \tCoPP violation %s on module %s: %s",
                    cmap,
                    module,
                    violations,
                )
    if not issue_found:
        log.info("[DEV] \tNo non-zero CoPP violation counters")

def report_intf_status(interfaces):
    issue_found = False
    for interface in interfaces.keys():
        if "err-disabled" in interfaces[interface]["status"]["state"]:
            issue_found = True
            log.error("[DEV] \tUnexpected status '%s' for interface %s", interfaces[interface]["status"]["state"], interface)
    if not issue_found:
        log.info("[DEV] \tNo interfaces in an unexpected status")

def configure_logging(debug_enabled):
    default_cfg = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)-15s %(levelname)-8s [%(funcName)20s] %(message)s"
            },
        },
        "handlers": {
            "console": {
                "level": "DEBUG",
                "formatter": "standard",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
            "logfile": {
                "level": "DEBUG",
                "formatter": "standard",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "{}.log".format(__name__),
                "maxBytes": 10000000,
            },
        },
        "loggers": {
            __name__: {
                "handlers": ["console", "logfile"],
                "level": "INFO",
                "propagate": False,
            },
        },
    }
    if debug_enabled:
        default_cfg["loggers"][__name__]["level"] = "DEBUG"
    logging.config.dictConfig(default_cfg)
    return logging.getLogger(__name__)


log = configure_logging(DEBUG)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
