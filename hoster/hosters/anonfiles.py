import json
import requests

from hoster.base_hoster import Hoster

class AnonfilesHoster(Hoster):

    def __init__(self):
        super().__init__(
            upload_url="https://api.anonfiles.com/upload",
            upload_url_keys=['data', 'file', 'url', 'short'],
            success_keys=['status'],
            success_values=[True]
        )

    def upload(self, file_path):
        with open(file_path, 'rb') as file:
            response = requests.post(self.upload_url, files={'file': file}, timeout=10)
            if response.status_code == 200:
                return self.process_response(response)
            else:
                return False, None

    def process_response(self, response):
        json_data = json.loads(response.content)
        download_url = self._get_value_from_json(json_data, self.upload_url_keys)
        success = self._get_value_from_json(json_data, self.success_keys)
        if success and self.is_valid_url(download_url):
            return success, download_url
        else:
            return False, None