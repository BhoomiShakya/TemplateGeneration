import os
import shutil
import subprocess
import pexpect


def read_file(path: str) -> str:
    """Reads and returns the contents of a file.

    Args:
        path (str): The path to the file to read.

    Returns:
        str: The contents of the file if it exists.
             Returns an error message if the file is not found.
    """
    if not os.path.exists(path):
        return f"File not found: {path}"
    with open(path, 'r') as file:
        return file.read()