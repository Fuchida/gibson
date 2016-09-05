import os
import re

import markdown
from flask import Markup

from config import GIT_REPO_DIR_PATH, ACCEPTED_FILE_FORMATS
from gitmanager import git_update, check_local_repo

# Global Config
DATA_DIR_PATH = GIT_REPO_DIR_PATH
FILE_DOT_MD_REGEX = ACCEPTED_FILE_FORMATS


class DataStore(object):
    """
        Class to access data
    """

    def __init__(self):
        super(DataStore, self).__init__()
        self.data = {}
        self.metadata = []
        check_local_repo()
        self.load_files()

    def load_files(self):
        """
        Load files from data_dir with markdown format and return a map with key as filename and value as contents
        """
        print("loading files ...")
        data = {}
        files_in_dir = os.listdir(DATA_DIR_PATH)
        for f in files_in_dir:
            # safegaurd to load only *.md files
            if re.match(FILE_DOT_MD_REGEX, f) is not None:
                # Read each file and save it's content in a dict with key as filename and value as content
                with open(DATA_DIR_PATH + "/" + f) as fp:
                        metadata = {}
                        mkd = markdown.Markdown(extensions=['markdown.extensions.meta'])

                        file_name = f.replace(".md", "")
                        value = fp.read()

                        parsed_mkd = mkd.convert(value)
                        data[file_name] = Markup(parsed_mkd)

                        for key, value in mkd.Meta.items():
                            metadata[key] = ' '.join(value)
                            metadata['file'] = file_name
                            metadata['url'] = file_name

                        # Only appends when we were able to extract metadata
                        if metadata:
                            self.metadata.append(metadata)
        self.data = data

    def get_data(self):
        """
            Function to access data, this is usually called
        """
        return self.data

    def get_metadata(self):
        """
            Function to fetch metadata
        """
        self.metadata.sort(key=lambda item: item['date'], reverse=True)
        return self.metadata

    def reload_data(self):
        """
            Reload data from DATA_DIR_PATH, usually called when changes are made
        """
        self.load_files()

    def reload(self):
        """
            Reload data
        """
        try:
            git_update()
        except Exception:
            print("Reload failed")
        finally:
            self.reload_data()
