import json
from hoster.base_hoster import Hoster

class FileIoHoster(Hoster):

    def __init__(self):
        super().__init__(
            upload_url="https://file.io",
            upload_url_keys=['link'],
            success_keys=['success'],
            success_values=[True]
        )

    def process_response(self, response):
        json_data = json.loads(response.text)
        success = self.success_values == [json_data.get(key) for key in self.success_keys]
        download_url = None
        if success:
            download_url = json_data.get(self.upload_url_keys[0])
        else:
            return False, None

        if self.is_valid_url(download_url):
            return success, download_url
        else:
            return False, None