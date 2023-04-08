import os
import requests
from hoster.base_hoster import Hoster

class KeepShHoster(Hoster):

    def __init__(self, bucket_name='free'):
        super().__init__(
            upload_url=f'https://{bucket_name}.keep.sh',
            upload_url_keys=None,
            success_keys=None,
            success_values=None
        )
        self.bucket_name = bucket_name

    def upload(self, file_path):
        with open(file_path, 'rb') as file:
            file_name = os.path.basename(file_path)
            headers = {'User-Agent': 'curl/7.81.0'}
            response = requests.put(f"{self.upload_url}/{file_name}", data=file, headers=headers, timeout=10)
            if response.status_code == 200:
                return self.process_response(response)
            else:
                return False, None

    def process_response(self, response):
        try:
            response.raise_for_status()
            download_url = response.text.strip()
            if self.is_valid_url(download_url):
                return True, download_url
            else:
                return False, None
        except requests.exceptions.HTTPError:
            return False, None
