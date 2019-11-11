# import pytest
# from mock import mock_open, patch
# from nxos_health_check import health_check

# class TestConfigFile:
#     @patch("builtins.open", new_callable=mock_open, read_data="""[Devices]\ntest1 = 192.0.2.1\ntest2 = 192.0.2.2\ntest3 = 192.0.2.3\n[Credentials]\nusername = test\npassword = test""")
#     def test_basic_config(self, mock_file):
#         devices = []
#         credentials = {"username": None, "password": None}
#         health_check.analyze_configuration(devices, credentials)

#         mock_file.assert_called_with("/app/config.ini")
#         assert devices[0]["name"] == "test1"
#         assert devices[0]["ip"] == "192.0.2.1"
#         assert devices[1]["name"] == "test2"
#         assert devices[1]["ip"] == "192.0.2.2"
#         assert devices[2]["name"] == "test3"
#         assert devices[2]["ip"] == "192.0.2.3"
