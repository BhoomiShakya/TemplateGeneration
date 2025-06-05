# tools/exit_loop.py

from google.adk.types import ToolContext

def exit_loop(tool_context: ToolContext) -> str:
    """Triggers the termination of a LoopAgent by setting escalate=True.

    Args:
        tool_context (ToolContext): The execution context of the agent tool call.

    Returns:
        str: A message indicating that the loop exit has been triggered.
    """
    print(f"[Tool Call] exit_loop triggered by {tool_context.agent_name}")
    tool_context.actions.escalate = True
    return f"✅ Loop exit triggered by {tool_context.agent_name}"
