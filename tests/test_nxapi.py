import pytest
import responses
from nxos_health_check import nxapi


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
