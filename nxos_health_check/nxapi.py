import requests
import json


class NXAPI:
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        self.base_url = f"https://{self.ip}/"
        self.url = f"{self.base_url}ins"
        requests.packages.urllib3.disable_warnings(
            requests.packages.urllib3.exceptions.InsecureRequestWarning
        )

    def _send_request(self, payload):
        headers = {
            "content-type": "application/json",
        }
        response = requests.post(
            self.url,
            data=json.dumps(payload),
            headers=headers,
            auth=(self.username, self.password),
            verify=False,
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

    def send_show_command(self, command):
        payload = self._format_show_command_payload(command)
        return self._send_request(payload)
