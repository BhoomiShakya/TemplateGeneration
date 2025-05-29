import os
import shutil
import subprocess
import pexpect


def create_file(path: str, content: str) -> str:
    """Creates a file at the specified path. Writes content to it.

    Args:
        path (str): The path where the file should be created.
        content (str): The content to write to the file.

    Returns:
        str: A confirmation message indicating what was done.
    """
    with open(path, 'w') as file:
        file.write(content)

    return (
        f"File created at {path} with content."
        if content
        else f"Empty file created at {path}."
    )