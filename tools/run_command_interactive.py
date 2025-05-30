import subprocess
from typing import Optional

def run_command_interactive(command: str, timeout: int = 60, input_text: Optional[str] = None) -> str:
    """
    Executes a shell command with optional input and timeout handling.

    Args:
        command (str): The shell command to execute.
        timeout (int): Timeout in seconds for command execution.
        input_text (str, optional): Input text to pass to the command (for prompts).

    Returns:
        str: Output or error message from the command.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            input=input_text,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout,
            check=False  # Don't raise exception automatically
        )
        output = result.stdout.strip()
        error = result.stderr.strip()
        return output if output else error
    except subprocess.TimeoutExpired:
        return "[ERROR] Command timed out. Use flags to avoid interaction."
    except Exception as e:
        return f"[ERROR] Unexpected error: {str(e)}"
