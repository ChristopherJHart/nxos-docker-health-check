import pytest
import responses
from nxos_health_check import nxapi
from .models import nxapi_expected_outputs


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
