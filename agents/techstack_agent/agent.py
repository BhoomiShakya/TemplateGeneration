from google.adk.agents import Agent
from google.adk.tools import google_search

techstack_agent = Agent(
    name="techstack_agent",
    model="gemini-2.0-flash",
    description="Provides setup instructions for tech stacks by performing real-time web search.",
    instruction=(
        "You are a helpful developer assistant. "
        "When the user provides a tech stack (e.g., 'React with Tailwind'), "
        "use the google_search tool to find the official setup steps from documentation or trusted sources. "
        "Then extract and present the steps **in a clear, markdown-formatted bullet list**.\n\n"
        "- If the steps are sequential, number them. If not, use bullet points.\n"
        "- Group related steps logically.\n"
        "- At the end, include a clearly labeled section called `.gitignore` with appropriate content "
        "for the selected stack (e.g., Node.js, Python, etc.). This is important for setting up version control correctly.\n\n"
        "Respond only with the setup steps and `.gitignore` section — no additional commentary or chit-chat."
    ),
    tools=[google_search],
    output_key="techstack_output"
)


root_agent = techstack_agent
