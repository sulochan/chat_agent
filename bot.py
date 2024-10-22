from agent import Agent

from common.client_utils import *  # noqa: F403

from multi_turn import *  # noqa: F403

from common.client_utils import *  # noqa: F403

CHATBOT = Agent("localhost", 5000)


async def chat(user_message: str):
    user_turn_input = prompt_to_turn(user_message)
    response = await execute_turns(
        agent_config=CHATBOT.agent_config,
        custom_tools=CHATBOT.tool_definitions,
        turn_inputs=[
            user_turn_input,
        ],
        host=CHATBOT.host,
        port=CHATBOT.port,
    )
    return response
