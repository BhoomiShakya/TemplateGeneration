import os
import shutil
import subprocess
import pexpect

def delete_folder(path: str) -> str:
    """Deletes the folder at the specified path.

    Args:
        path (str): The path to the folder to delete.

    Returns:
        str: A message indicating whether the folder was deleted or not found.
    """
    if os.path.exists(path) and os.path.isdir(path):
        shutil.rmtree(path)
        return f"Folder deleted: {path}"
    return f"Folder does not exist: {path}"