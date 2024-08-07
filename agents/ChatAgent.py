from langchain.agents import create_react_agent, initialize_agent, create_structured_chat_agent
from langchain.agents.react.output_parser import ReActOutputParser
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import render_text_description_and_args

from tools.eme_task import CreateTask
from tools.words_len_tool import Calculate

llm = ChatOllama(model='qwen2:7b-instruct', strea)

conversation_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True
)

tools = [
    Calculate(),
    CreateTask()
]

template = '''你作为一个应急领域专家，有权限使用以下工具来完成任务:

            {tools}

            如果要调用工具的话，使用如下格式：
            Question: 需要你回答的问题
            Thought: 你应该时刻思考该做什么 
            Action: 要执行的方法，需要是工具列表 [{tool_names}] 中的一个
            Action Input: 要执行方法的参数，你需要给一个完整的JSON类型参数
            Observation: 方法执行的结果
            ... 可能会重复N次
            Final Answer: 原始问题的最终答案
            
            开始
            Question: {input}
            Thought:{agent_scratchpad}
            '''

prompt = PromptTemplate.from_template(template)

# agent = create_react_agent(llm=llm, tools=tools, prompt=prompt, tools_renderer=render_text_description_and_args)
agent = create_structured_chat_agent(llm=llm, tools=tools, prompt=prompt)

"""
agent = initialize_agent(
    agent='chat-conversational-react-description',
    # agent='openai-multi-functions',
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=3,
    early_stopping_method='generate',
    memory=conversation_memory
)
"""

resp = agent.invoke(input={'input': '给张三创建一个任务，让他去采购一些应急物资', 'intermediate_steps': ""})

print(resp)
