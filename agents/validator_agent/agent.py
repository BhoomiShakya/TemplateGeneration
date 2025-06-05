from google.adk.agents import Agent
from tools.read_file import read_file 
validator_agent = Agent(
    name="validator_agent",
    model="gemini-2.0-flash",
    description="Validates the generated project structure against techstack output.",
    instruction=(
        "Your task is to verify that the generated folder and file structure matches the instructions given by the `techstack_agent`.\n\n"
        "🔍 **Steps**:\n"
        "- Use `read_file(path)` to inspect key files (e.g., package.json, README.md, index.html).\n"
        "- Compare folder names, file names, and file content (commands, boilerplate, etc.) with the `techstack_output`.\n\n"
        "✅ If everything matches, respond with:\n"
        "`All files and structure are correct. No issues found.`\n\n"
        "❌ If there are problems, return a numbered list of issues in this format:\n"
        "`1. [Short issue title] - [What’s wrong]`\n"
        "`2. ...`\n\n"
        "Only list actual mismatches or errors that need fixing."
    ),
    tools=[read_file],
    output_key="error_report"
)

root_agent = validator_agent
