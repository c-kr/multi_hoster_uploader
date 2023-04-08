import json
from hoster.base_hoster import Hoster

class BayfilesHoster(Hoster):

    def __init__(self):
        super().__init__(
            upload_url="https://api.bayfiles.com/upload",
            upload_url_keys=['data', 'file', 'url', 'full'],
            success_keys=['status'],
            success_values=[True]
        )

    def process_response(self, response):
        json_data = json.loads(response.text)
        success = self.success_values == [json_data.get(key) for key in self.success_keys]
        download_url = None
        if success:
            current_data = json_data
            for key in self.upload_url_keys:
                current_data = current_data.get(key)
            download_url = current_data
        else:
            return False, None

        if self.is_valid_url(download_url):
            return success, download_url
        else:
            return False, None