from typing import Any

from task.tools.deployment.base_agent_tool import BaseAgentTool


class WebSearchAgentTool(BaseAgentTool):

    # TODO:
    # Provide implementations of deployment_name (in core config), name, description and parameters.
    # Don't forget to mark them as @property
    # Parameters:
    #   - prompt: string. Required.
    #   - propagate_history: boolean

    @property
    def deployment_name(self) -> str:
        return "web-search-agent"

    @property
    def name(self) -> str:
        return "web_search_agent"

    @property
    def description(self) -> str:
        return "Agent that can perform web search to find necessary information, verify facts, and synthesize information from multiple sources"

    @property
    def parameters(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string",
                    "description": "The query or instruction to send to the WEB Search Agent.",
                },
                "propagate_history": {
                    "type": "boolean",
                    "default": False,
                    "description": (
                        """
                        To to include previous conversation history between the current agent and Content Management Agent
                        When `true` is provided, history context will be shared with agent.
                        When `false` is provided, not history context is shared.
                        Set as `true`, only when the `prompt` lacks sufficient context.
                        """
                    ),
                },
            },
            "required": ["prompt"],
        }
