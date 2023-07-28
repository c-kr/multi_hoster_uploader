import json
import requests

from hoster.base_hoster import Hoster

class AnonAndCoHoster(Hoster):
    def __init__(self, upload_url):
        super().__init__(upload_url=upload_url, upload_url_keys=['data', 'file', 'url', 'short'], success_keys = ['status'], success_values=[True])

    def process_response(self, response):
        json_data = json.loads(response.content)
        download_url = self._get_value_from_json(json_data, self.upload_url_keys)
        success = self._get_value_from_json(json_data, self.success_keys)
        if success and self.is_valid_url(download_url):
            return success, download_url
        else:
            return False, None

class AnonfilesHoster(AnonAndCoHoster):

    def __init__(self):
        super().__init__(
            upload_url="https://api.anonfiles.com/upload"
        )

class BayfilesHoster(AnonAndCoHoster):

    def __init__(self):
        super().__init__(
            upload_url="https://api.bayfiles.com/upload",
        )

class FilechanHoster(AnonAndCoHoster):

    def __init__(self):
        super().__init__(
            upload_url="https://api.filechan.org/upload",
        )

class HotfileHoster(AnonAndCoHoster):

    def __init__(self):
        super().__init__(
            upload_url="https://api.hotfile.io/upload",
        )

class LetsuploadHoster(AnonAndCoHoster):

    def __init__(self):
        super().__init__(
            upload_url="https://api.letsupload.cc/upload",
        )

class LolabitsHoster(AnonAndCoHoster):

    def __init__(self):
        super().__init__(
            upload_url="https://api.lolabits.se/upload",
        )

class MegauploadHoster(AnonAndCoHoster):

    def __init__(self):
        super().__init__(
            upload_url="https://api.megaupload.nz/upload",
        )

class MyfileHoster(AnonAndCoHoster):

    def __init__(self):
        super().__init__(
            upload_url="https://api.myfile.is/upload",
        )

class OpenloadHoster(AnonAndCoHoster):

    def __init__(self):
        super().__init__(
            upload_url="https://api.openload.cc/upload",
        )

class RapidshareHoster(AnonAndCoHoster):

    def __init__(self):
        super().__init__(
            upload_url="https://api.rapidshare.nu/upload",
        )

class ShareonlineHoster(AnonAndCoHoster):

    def __init__(self):
        super().__init__(
            upload_url="https://api.share-online.is/upload",
        )

class UpvidHoster(AnonAndCoHoster):

    def __init__(self):
        super().__init__(
            upload_url="https://api.upvid.cc/upload",
        )

class VshareHoster(AnonAndCoHoster):

    def __init__(self):
        super().__init__(
            upload_url="https://api.vshare.is/upload",
        )

class ZippyshareHoster(AnonAndCoHoster):

    def __init__(self):
        super().__init__(
            upload_url="https://api.zippysha.re/upload",
        )