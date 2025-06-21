from google.adk.agents import SequentialAgent
from agents.filesystem_agent.agent import filesystem_agent
from agents.techstack_agent.agent import techstack_agent
from agents.ROOT_Loop_Agent.agent import ROOT_Loop_Agent
# from agents.ReadMe_agent.agent import ReadMe_agent  

ROOT_Agent = SequentialAgent(
    name="ROOT_Agent",
    description="Handles a full Template Generation system interaction pipeline.",
    sub_agents=[techstack_agent, filesystem_agent, ROOT_Loop_Agent],
)

root_agent = ROOT_Agent