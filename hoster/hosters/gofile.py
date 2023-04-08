from hoster.base_hoster import Hoster
import requests

class GofileHoster(Hoster):
    def __init__(self):
        super().__init__(
            upload_url="https://{server}.gofile.io/uploadFile",
            upload_url_keys=['data', 'downloadPage'],
            success_keys=['status'],
            success_values=['ok']
        )

    def upload(self, file_path):
        server = self._get_server()
        self.upload_url = self.upload_url.replace("{server}", server)

        return super().upload(file_path)

    def _get_server(self):
        response = requests.get("https://api.gofile.io/getServer", timeout=10)
        data = response.json()
        if data.get("status") == "ok":
            return data["data"]["server"]
        else:
            raise Exception("Failed to get Gofile server")

    def process_response(self, response):
        data = response.json()
        success = all(data.get(key) == value for key, value in zip(self.success_keys, self.success_values))
        download_url = self._get_value_from_json(data, self.upload_url_keys) if success else None
        if self.is_valid_url(download_url):
            return success, download_url
        else:
            return False, None