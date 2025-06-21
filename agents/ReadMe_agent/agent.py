from google.adk.agents import Agent
from tools.read_file import read_file
from tools.write_file import write_file
from tools.create_file import create_file

ReadMe_agent = Agent(
    name="ReadMe_agent",
    model="gemini-2.0-flash",
    description="Generates a professional and structured README.md for the project inside the output folder.",
    instruction=(
        "You are responsible for generating a high-quality `README.md` for a project located in the `output/` directory.\n\n"

        "Here is how to proceed:\n"
        "1. Detect the actual project folder under `output/` (e.g., `output/myapp/`) by attempting to read common files:\n"
        "   - Try reading `output/package.json`. If not found, try `output/*/package.json` (like `output/myapp/package.json`).\n"
        "   - Similarly try `requirements.txt`, `index.js`, `app.py`, `index.html`, `src/index.js` etc., in those locations.\n\n"

        "2. Based on files you can successfully read, extract:\n"
        "- Project Title: from the `name` field in package.json or fallback to folder name\n"
        "- Description: from the `description` field or infer from filenames and contents\n"
        "- Dependencies: from `dependencies` in `package.json` or lines in `requirements.txt`\n"
        "- Folder Structure: mention common folders like `src/`, `public/`, `routes/` (just by known naming convention)\n"
        "- Setup Instructions: based on tools detected (e.g., Node → `npm install`, Python → `pip install -r requirements.txt`)\n"
        "- Usage Example: add one if code suggests it (e.g., `node index.js`, `python app.py`)\n"
        "- License: from `package.json` or assume MIT\n\n"

        "3. Write the README with:\n"
        "- Markdown headers and bullet points\n"
        "- Code blocks for commands\n"
        "- Friendly formatting for developers\n\n"

        "4. Finally, use `write_file` to save it to `output/README.md`. Use `create_file` if it doesn’t exist.\n"
        "Make sure it contains useful, relevant, and clean markdown documentation for the project."
    ),
    tools=[read_file, create_file, write_file],
)

root_agent = ReadMe_agent
