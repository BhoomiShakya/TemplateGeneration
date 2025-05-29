import os
import shutil
import subprocess
import pexpect

def run_command_interactive(command: str, timeout: int = 30) -> str:
    """
    Executes a shell command and interacts with prompts using AI feedback loops.
    """
    try:
        child = pexpect.spawn(command, encoding='utf-8', timeout=timeout)
        output = ""

        while True:
            i = child.expect([pexpect.EOF, pexpect.TIMEOUT, r'[\?\:>]'])  # Detect prompt-like patterns
            output += child.before

            if i == 0:  # EOF
                break
            elif i == 1:  # Timeout
                output += "\n[Timeout waiting for input]\n"
                break
            elif i == 2:  # Detected prompt
                prompt = child.after.strip()
                # Return the prompt to the model for a response
                return f"[PROMPT] {prompt}\n{output}"

        return output.strip()

    except Exception as e:
        return f"[ERROR] {str(e)}"