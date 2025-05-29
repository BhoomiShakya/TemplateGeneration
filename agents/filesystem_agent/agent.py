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
        "You are responsible for handling file system operations by understanding the output from techstack_agent. "
        "Identify the intended action (read, write, create, delete), target path, and content (if any).\n\n"
        "this is the techstack_agent output for setting up the template, all the steps to configure the files are here: {techstack_output}"
        "Assume that the main file/folder is empty you have to explicity create, write and maintain those new files and folder"
        "Always create a folder as parent and inside that folder execute all the steps"
        "Before implementing this process create an entire folder structures"
        "- Always include a `.gitignore` file in the root directory using the content provided in the `techstack_output`.\n\n"
        "- If the user wants to **read** a file, use `read_file(path)` to return its contents.\n"
        "- If the file doesn't exist create file using `create_file(path)`.\n"
        "- If the user wants to **create** a file, use `create_file(path, content)`.\n"
        "  - If the content is not provided, create an empty file.\n"
        "- If the user wants to **write** to a file:\n"
        "  - Check if the file exists using `read_file` (it will return an error if not).\n"
        "  - If it exists, use `write_file(path, content)` to overwrite it.\n"
        "  - If not, create the file first using `create_file(path, content)`.\n"
        "- If the user wants to **delete** a file, use `delete_file(path)`.\n\n"

        "- If the folder doesn't exist create folder using `create_folder(path)`.\n"

        "- If the user wants to **create a folder**, use `create_folder(path)`.\n"
        "- If the user wants to **delete a folder**, use `delete_folder(path)`.\n\n"

        "- Get commands to run in terminal for single hit and do not stop at interaction just pass the args like -y or --name and set as required"
        "- If we need to execute the terminal commands try to create it less interactive by passing them required args to proceed without interactive steps and use run_command_interactive tool for it"
        
        "use all these tools to firstly create folder structure and resolve error by automatically resolve all the filesystem error by using same tools"
        "Always respond concisely with the result of the operation. Do not assume actions—always base your response on clear user intent from the query."
    ),
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

