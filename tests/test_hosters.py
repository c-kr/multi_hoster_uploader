import unittest
import os
from hoster.hosters import AnonfilesHoster, BayfilesHoster, FileIoHoster, GofileHoster, KeepShHoster

class TestHosters(unittest.TestCase):

    def setUp(self):
        self.file_path = 'test_file.txt'
        self.anonfiles_hoster = AnonfilesHoster()
        self.bayfiles_hoster = BayfilesHoster()
        self.file_io_hoster = FileIoHoster()
        self.gofile_hoster = GofileHoster()
        self.keepsh_hoster = KeepShHoster()

        # Create a test file for uploading
        with open(self.file_path, 'w') as f:
            f.write('This is a test file.')

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def _assert_upload(self, hoster):
        success, upload_url = hoster.upload(self.file_path)
        self.assertTrue(success)
        self.assertIsNotNone(upload_url)
        self.assertTrue(upload_url.startswith("https"))

    def test_anonfiles_upload(self):
        self._assert_upload(self.anonfiles_hoster)

    def test_bayfiles_upload(self):
        self._assert_upload(self.bayfiles_hoster)

    def test_file_io_upload(self):
        self._assert_upload(self.file_io_hoster)

    def test_gofile_upload(self):
        self._assert_upload(self.gofile_hoster)

    def test_keepsh_upload(self):
        self._assert_upload(self.keepsh_hoster)

if __name__ == '__main__':
    unittest.main()
