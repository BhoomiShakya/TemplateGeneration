import os
import shutil
import subprocess
import pexpect

def create_folder(path: str) -> str:
    """Creates a folder at the specified path.

    Args:
        path (str): The path where the folder should be created.

    Returns:
        str: A confirmation message indicating whether the folder was created or already exists.
    """
    try:
        os.makedirs(path, exist_ok=True)
        return f"Folder created at {path}" if not os.path.exists(path) else f"Folder already exists at {path}"
    except Exception as e:
        return f"Failed to create folder: {e}"
