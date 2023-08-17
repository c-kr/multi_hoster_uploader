from hoster.base_hoster import Hoster
from random import shuffle
from typing import List, Optional, Type, Union
from pathlib import Path


class MultiHosterManager:
    def __init__(self, hosters: List[Type[Hoster]], random_hoster: bool = False):
        """
        Initialize the MultiHosterManager class.

        :param hosters: A list of Hoster classes (not instances).
        :param random_hoster: Optional, if True, the hosters will be shuffled before each upload. Defaults to False.
        """
        if not hosters:
            raise ValueError("Hoster list is empty. Please provide at least one Hoster class.")

        self.hosters = []
        self.random_hoster = random_hoster

        for hoster in hosters:
            if issubclass(hoster, Hoster):
                self.hosters.append(hoster())
            else:
                raise TypeError(f"Invalid hoster element: {hoster}. It should be a subclass of Hoster.")

    def upload(self, file_path: Union[str, Path]) -> Optional[str]:
        """
        Upload a file to one of the hosters in the manager.

        :param file_path: The path to the file to be uploaded.
        :return: The download URL of the uploaded file if the upload was successful, None otherwise.
        """
        if self.random_hoster:
            shuffle(self.hosters)
        for hoster in self.hosters:
            try:
                print(f"Uploading {file_path} to {hoster.__class__.__name__}...")
                success, download_url = hoster.upload(file_path)
                if success:
                    return download_url
            except Exception as e:
                print(f"An error occurred while uploading to {hoster.__class__.__name__}: {e}")
                continue
        return None
