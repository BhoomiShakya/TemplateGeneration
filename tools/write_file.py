import os
import shutil
import subprocess
import pexpect


def write_file(path: str, content: str) -> str:
    """Writes content to the file at the specified path.

    Args:
        path (str): The path to the file where content should be written.
        content (str): The content to write to the file.

    Returns:
        str: A confirmation message indicating the content was written.
    """
    with open(path, 'w') as file:
        file.write(content)
    return f"Content written to {path}"