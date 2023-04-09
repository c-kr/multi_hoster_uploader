# Multi Hoster Uploader

Multi Hoster Uploader serves as both a command-line tool and a Python package for uploading files to multiple file hosting services. It enables easy and efficient file uploads to various hosting services by trying them in a predefined or random order. If one hoster fails for any reason, the next hoster in the list is tried.

## Table of Contents

- [Hoster Status](#hoster-status)
- [Installation](#installation)
- [Usage](#usage)
- [Using MultiHosterManager in Your Own Script](#using-multihostermanager-in-your-own-script)
- [Developing Custom Hoster Classes](#developing-custom-hoster-classes)
- [Acknowledgments](#acknowledgments)
- [License](#license)

# Hoster Status

| Hoster                                                                                                  | Status                                                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <img src="https://anonfiles.com/favicon.ico" width="16" height="16" alt="Anonfiles Favicon"> Anonfiles  | [![Anonfiles](https://github.com/c-kr/multi_hoster_uploader/actions/workflows/test-anonfile.yml/badge.svg)](https://github.com/c-kr/multi_hoster_uploader/actions/workflows/test-anonfile.yml) |
| <img src="https://bayfiles.com/favicon.ico" width="16" height="16" alt="Bayfiles Favicon"> Bayfiles     | [![Bayfiles](https://github.com/c-kr/multi_hoster_uploader/actions/workflows/test-bayfiles.yml/badge.svg)](https://github.com/c-kr/multi_hoster_uploader/actions/workflows/test-bayfiles.yml)  |
| <img src="https://www.file.io/favicon.ico" width="16" height="16" alt="FileIo Favicon"> FileIo          | [![FileIO](https://github.com/c-kr/multi_hoster_uploader/actions/workflows/test-file_io.yml/badge.svg)](https://github.com/c-kr/multi_hoster_uploader/actions/workflows/test-file_io.yml)      |
| <img src="https://gofile.io/dist/img/favicon16.png" width="16" height="16" alt="Gofile Favicon"> GoFile | [![GoFile](https://github.com/c-kr/multi_hoster_uploader/actions/workflows/test-gofile.yml/badge.svg)](https://github.com/c-kr/multi_hoster_uploader/actions/workflows/test-gofile.yml)        |
| KeepSh                                                                                                  | [![KeepSh](https://github.com/c-kr/multi_hoster_uploader/actions/workflows/test-keepsh.yml/badge.svg)](https://github.com/c-kr/multi_hoster_uploader/actions/workflows/test-keepsh.yml)        |


## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/c-kr/multi_hoster_uploader.git
   ```
2. Change into the project directory:
   ```bash
   cd multi_hoster_uploader
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Optionally symlink the CLI Tool to your PATH
   ```bash
   ln -s /path/to/multi_hoster_uploader/multi_hoster_uploader ~/.local/bin/multi_hoster_uploader
   ```

## Usage

Upload a file using the default hosters and order:
```bash
multi_hoster_uploader --file /path/to/your/file.txt
```

Upload a file using a random hoster order:
```bash
multi_hoster_uploader --file /path/to/your/file.txt --random-hoster
```

To modify the default hoster sequence, adjust the HOSTERS variable within the multi_hoster_uploader file.

## Using MultiHosterManager in Your Own Script

To use the `MultiHosterManager` class in your own script, follow these steps:

1. Import the `MultiHosterManager` class and the hoster classes you want to use:

```python
from hoster import MultiHosterManager
from hoster.hosters import AnonfilesHoster, BayfilesHoster, FileIoHoster, GofileHoster, KeepShHoster
```
   
Instantiate the MultiHosterManager class with the list of hoster classes and, optionally, a flag to randomize the hoster order:

```python
manager = MultiHosterManager([FileIoHoster, GofileHoster, BayfilesHoster, KeepShHoster, AnonfilesHoster], random_hoster=True)
```

Call the upload method of the MultiHosterManager instance, providing the file path as an argument:

```python
download_url = manager.upload('/path/to/your/file.txt')
```

## Developing Custom Hoster Classes

To develop custom hoster classes, follow these steps:

1. Create a new Python file for your custom hoster class in the `hoster/hosters` directory.
2. Import the `Hoster` base class from `hoster.base_hoster`.
3. Create a new class that inherits from `Hoster` and implement the required methods, such as `upload` and `process_response`.
4. Add your custom hoster class to the `HOSTERS` list in the `multi_hoster_uploader` script.
5. Extend Unittest, Github Workflow and README.md
6. Open a Github Pull Request if you want to share your hoster class

For more information on creating custom hoster classes, refer to the existing hoster classes in the `hoster/hosters` directory.

## Acknowledgments

I would like to acknowledge the contribution of GPT-4 by OpenAI in the development of various parts of the Multi Hoster Uploader.

## License

[MIT](https://choosealicense.com/licenses/mit/)

