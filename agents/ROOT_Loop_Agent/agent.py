from google.adk.agents import LoopAgent
from agents.validator_agent.agent import validator_agent
from agents.refactor_agent.agent import refactor_agent

ROOT_Loop_Agent = LoopAgent(
    name="ROOT_Loop_Agent",
    description=(
        "This loop agent ensures the generated project structure is correct by running a validation-refactor cycle. "
        "It first uses `validator_agent` to detect mismatches between the actual file system and the expected setup "
        "described in the `techstack_output`. If issues are found, `refactor_agent` is triggered to correct them. "
        "This process is repeated up to 5 times or until no more issues are found."
    ),
    sub_agents=[validator_agent, refactor_agent],
    max_iterations=5
)


root_agent = ROOT_Loop_Agent