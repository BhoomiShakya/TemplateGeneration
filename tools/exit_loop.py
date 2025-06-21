def exit_loop(tool_context) -> dict:
    """Triggers the termination of a LoopAgent by setting escalate=True.

    Args:
        tool_context: The execution context of the agent tool call.

    Returns:
        dict: An empty dictionary to indicate tool completion.
    """
    print(f"[Tool Call] exit_loop triggered by {tool_context.agent_name}")
    tool_context.actions.escalate = True
    return {}
