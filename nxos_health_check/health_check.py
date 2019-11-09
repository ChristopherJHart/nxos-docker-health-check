import sys
import os
import logging
import logging.config
import requests
from nxapi import NXAPI


__author__ = "Christopher Hart"
__email__ = "chart2@cisco.com"
__copyright__ = "Copyright (c) 2019 Cisco Systems. All rights reserved."
__credits__ = ["Christopher Hart",]
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

NXAPI_IP = os.getenv("NXAPI_IP")
NXAPI_USERNAME = os.getenv("NXAPI_USERNAME")
NXAPI_PASSWORD = os.getenv("NXAPI_PASSWORD")
DEBUG = os.getenv("DEBUG")

def main():
    log.info("[INIT] Initializing health check")
    log.info("[VAR] IP: %s", NXAPI_IP)
    log.info("[VAR] Username: %s", NXAPI_USERNAME)
    log.info("[VAR] Password: %s", NXAPI_PASSWORD)
    nxapi_conn = NXAPI(NXAPI_IP, NXAPI_USERNAME, NXAPI_PASSWORD)
    output = nxapi_conn.send_show_command("show module")
    log.info(output)

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
            }
        },
        "loggers": {
            __name__: {
                "handlers": ["console", "logfile"],
                "level": "INFO",
                "propagate": False
            },
        }
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