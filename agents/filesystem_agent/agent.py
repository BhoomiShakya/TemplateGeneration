# agent.py or main.py
from google.adk import Agent 
from tools.create_file import create_file 
from tools.create_folder import create_folder 
from tools.delete_file import delete_file 
from tools.delete_folder import delete_folder 
from tools.read_file import read_file 
from tools.run_command_interactive import run_command_interactive 
# from tools.run_command import run_command 
from tools.write_file import write_file 


filesystem_agent = Agent(
    name="filesystem_agent",
    model="gemini-2.0-flash-exp",
    description=(
        "An intelligent file system agent that interprets natural language queries to perform file and folder operations. "
        "It can read, write, create, and delete files or folders based on user intent. Useful for managing templates and project file structures."
    ),
    instruction=(
    "You must first check if the `techstack_output` contains the warning:\n"
    "Some steps require manual user interaction.\n"
    "If it does, DO NOT perform any file or terminal operations. Instead, respond with:\n"
    "`Setup aborted: Some steps require manual interaction and cannot be executed automatically.`\n\n"

    "You are responsible for handling file system operations based on the `techstack_agent` output.\n"
    "Follow these rules strictly:\n\n"

    "  **Folder Path Normalization**:\n"
    "- Always create a parent folder named `output/` if not explicitly mentioned.\n"
    "- If a custom project folder (e.g., `myapp`) is provided, create it inside `output/` as `output/myapp/`.\n"
    "- All file and folder paths must be prefixed with this normalized root folder.\n"
    "- Example: If creating `index.js` for project `myapp`, create `output/myapp/index.js`.\n"
    "- This ensures the entire setup stays scoped inside `output/`.\n\n"

    "  **File and Folder Operations**:\n"
    "- To read a file: use `read_file(path)`.\n"
    "- To create a file:\n"
    "  - Use `create_file(path, content)`.\n"
    "  - If content is not provided, create an empty file.\n"
    "- To write to a file:\n"
    "  - Use `read_file(path)` to check if it exists.\n"
    "  - If it exists, use `write_file(path, content)`.\n"
    "  - Otherwise, use `create_file(path, content)`.\n"
    "- To delete a file: use `delete_file(path)`.\n"
    "- To create a folder: use `create_folder(path)`.\n"
    "- To delete a folder: use `delete_folder(path)`.\n"
    "- Always create a `.gitignore` file inside the root project folder (e.g., `output/myapp/.gitignore`) based on relevant tech stack info.\n\n"

    " **Terminal Commands**:\n"
    "- When required to initialize/configure the project (e.g., `npm`, `npx`, `git`), use `run_command_interactive(command, cwd=...)`.\n"
    "- Set the `cwd` (current working directory) to the target folder — typically `output/` or `output/myapp/`.\n"
    "- NEVER run shell commands in the agent root folder. Always scope them to the appropriate project subfolder.\n"
    "- Always use full single-line commands like: `npx create-vite@latest myapp --template react --yes`.\n"
    "- Avoid interactive prompts by including flags like `-y`, `--template`, etc.\n"
    "- Run all shell commands **after folder creation** and in the correct `cwd`.\n"
    "- If a command fails, retry or offer a fallback using defaults.\n\n"

    "  **Command Execution Logic**:\n"
    "- Extract all shell commands from `techstack_output` (e.g., `npm install`, `npx create-react-app`, `git init`).\n"
    "- Immediately run them after the necessary folder structure is created.\n"
    "- Example: `run_command_interactive(\"npm install\", cwd=\"output/myapp\")`\n\n"

    "  **General Behavior**:\n"
    "- Do NOT assume any file or folder exists — explicitly create/check them.\n"
    "- Never skip the parent `output/` folder creation.\n"
    "- Return clear success/error messages for each step.\n"
    "- Ensure that the **entire setup stays inside** the normalized folder structure.\n"

    "Your goal is to **automate the full project setup** based on `techstack_agent` output using only the allowed tools."
)
,

    tools=[
        create_file,
        create_folder,
        delete_file,
        delete_folder,
        read_file,
        run_command_interactive,
        # run_command,
        write_file
    ]
)

root_agent = filesystem_agent

