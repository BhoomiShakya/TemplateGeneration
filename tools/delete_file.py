import os
import shutil
import subprocess
import pexpect

def delete_file(path: str) -> str:
    """Deletes the specified file if it exists.

    Args:
        path (str): The path to the file to delete.

    Returns:
        str: A message indicating whether the file was deleted or not found.
    """
    if os.path.exists(path):
        os.remove(path)
        return f"File deleted: {path}"
    return f"File does not exist: {path}"