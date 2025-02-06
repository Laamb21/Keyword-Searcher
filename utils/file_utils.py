# utils/file_utils.py

import os

def get_all_files(root_path):
    """
    Recursively traverse the directory and return a list of file paths.
    """
    file_paths = []
    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            file_paths.append(os.path.join(dirpath, filename))
    return file_paths
