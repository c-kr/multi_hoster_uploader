import requests
from urllib.parse import urlparse
from typing import Any, List, Tuple, Union
from pathlib import Path


class Hoster:
    def __init__(self, upload_url: str, upload_url_keys: List[str], success_keys: List[str], success_values: Union[List[Union[str, bool]], None] = None) -> None:
        """
        Initialize the Hoster class.

        :param upload_url: The URL to upload files to.
        :param upload_url_keys: A list of keys to access the upload URL in the JSON response.
        :param success_keys: A list of keys to check for a successful upload in the JSON response.
        :param success_values: Optional, a list of values for the success keys that indicates a successful upload. Defaults to None.
        """
        self.upload_url = upload_url
        self.upload_url_keys = upload_url_keys
        self.success_keys = success_keys
        self.success_values = success_values

    def upload(self, file_path: Union [str, Path]) -> Tuple[bool, Union[str, None]]:
        """
        Upload a file to the specified URL.

        :param file_path: The path to the file to be uploaded.
        :return: A tuple containing a boolean indicating if the upload was successful, and the download_url or None is not successful.
        """
        with open(file_path, 'rb') as file:
            response = requests.post(self.upload_url, files={'file': file}, timeout=10)
            if response.status_code == 200:
                return self.process_response(response)
            else:
                return False, None

    def process_response(self, response: requests.Response) -> Tuple[bool, Union[str, None]]:
        """
        Process the response after uploading the file. This method should be implemented by a subclass.

        :param response: A requests.Response object containing the response from the upload request.
        :return: A tuple containing a boolean indicating if the upload was successful, and the download_url or None is not successful.
        """
        raise NotImplementedError("This method should be implemented by a subclass.")

    @staticmethod
    def _get_value_from_json(data: dict, keys: List[str]) -> Any:
        """
        Retrieve a value from a nested JSON object using a list of keys.

        :param data: A dictionary representing a JSON object.
        :param keys: A list of keys to traverse the JSON object.
        :return: The value found in the JSON object or None if the keys do not lead to a valid value.
        """
        for key in keys:
            data = data.get(key)
            if data is None:
                return None
        return data

    @staticmethod
    def is_valid_url(url: str) -> bool:
        """
        Check if a given string is a valid URL.

        :param url: The URL string to be checked.
        :return: True if the URL is valid, False otherwise.
        """
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False
