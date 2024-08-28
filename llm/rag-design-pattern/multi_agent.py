from utils import get_openai_api_key
OPENAI_API_KEY = get_openai_api_key()
llm_config = {"model": "gpt-4o-mini"}

from autogen import ConversableAgent
import pprint


cathy = ConversableAgent(
    name="zhang_san",
    system_message=
    "你的名字是张三，你是一个相声演员",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

joe = ConversableAgent(
    name="li_si",
    system_message=
    "你的名字是李四，你是一个相声演员"
    "根据上一个笑料讲出下一个笑料",
    llm_config=llm_config,
    human_input_mode="NEVER",
)
chat_result = joe.initiate_chat(
    cathy, 
    message="我是李四. 让我们开始抖笑料吧，张三", 
    max_turns=2, 
    summary_method="reflection_with_llm",
    summary_prompt="Sumarize the conversation",
)
pprint.pprint(chat_result.chat_history)
pprint.pprint(chat_result.cost)
pprint.pprint(chat_result.summary)