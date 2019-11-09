import pytest
import responses
from nxos_health_check import nxapi
from .models.nxapi_expected_outputs import NXAPI_SHOW_MODULE_OUTPUT, NXAPI_SHOW_VERSION_OUTPUT

class TestNxapiInit:
    def test_basic_init(self):
        example_ip = "10.122.140.113"
        example_username = "admin"
        example_password = "cisco!123"
        example_base_url = "https://10.122.140.113/"
        example_url = "https://10.122.140.113/ins"
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
        example_ip = "10.122.140.113"
        example_username = "admin"
        example_password = "cisco!123"

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
        example_ip = "10.122.140.113"
        example_username = "admin"
        example_password = "cisco!123"

        nxapi_conn = nxapi.NXAPI(example_ip, example_username, example_password)
        returned_payload = nxapi_conn._format_show_command_payload(example_command)
        assert returned_payload == expected_payload


class TextNxapiShowCommands:
    def test_module_command(self):
        command = "show module"
        example_ip = "10.122.140.113"
        example_username = "admin"
        example_password = "cisco!123"

        expected_output = NXAPI_SHOW_MODULE_OUTPUT

        nxapi_conn = nxapi.NXAPI(example_ip, example_username, example_password)
        output = nxapi_conn.send_show_command(command)
        assert output is not None
        assert output == expected_output

    def test_version_command(self):
        command = "show version"
        example_ip = "10.122.140.113"
        example_username = "admin"
        example_password = "cisco!123"

        expected_output = NXAPI_SHOW_VERSION_OUTPUT

        nxapi_conn = nxapi.NXAPI(example_ip, example_username, example_password)
        output = nxapi_conn.send_show_command(command)
        assert output is not None
        assert output == expected_output