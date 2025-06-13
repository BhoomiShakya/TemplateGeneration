from google.adk.agents import Agent
from tools.create_file import create_file 
from tools.create_folder import create_folder 
from tools.delete_file import delete_file 
from tools.delete_folder import delete_folder 
from tools.read_file import read_file 
from tools.run_command_interactive import run_command_interactive 
from tools.write_file import write_file 
from tools.exit_loop import exit_loop

refactor_agent = Agent(
    name="refactor_agent",
    model="gemini-2.0-flash",
    description="Refactors the generated project structure based on validator issues.",
    instruction=(
        "You are responsible for fixing any issues in {{error_report}} reported by the `validator_agent`.\n\n"
        "🔧 **Steps**:\n"
        "- Use tools like `create_file`, `write_file`, `delete_file`, etc., to fix each issue in the `error_report`.\n"
        "- Always ensure changes follow the `techstack_output` instructions.\n"
        "- Confirm after each fix that the folder structure and file content are consistent.\n"
        "- Do not make assumptions. Only correct the reported problems.\n\n"
        "When all issues are fixed, respond: `All issues have been resolved.`"
       "If the message is exactly:\n"
        "`All files and structure are correct. No issues found.`\n\n"
        "You MUST call the 'exit_loop' tool. Do not output anything else.\n\n"
        "Otherwise, use your tools to fix the listed problems using the `techstack_output` as guidance."

    ),
    tools=[
        create_file,
        create_folder,
        delete_file,
        delete_folder,
        read_file,
        run_command_interactive,
        write_file,
        exit_loop
    ],
    output_key=None  # or omit if not needed
)



root_agent = refactor_agent
