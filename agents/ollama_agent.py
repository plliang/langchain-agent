"""
基于Ollama的聊天机器人
"""
from langchain.agents import create_react_agent, AgentExecutor
from langchain.agents.chat.base import ChatAgent
from langchain.agents.output_parsers import ReActSingleInputOutputParser
from langchain.agents.react.output_parser import ReActOutputParser
from langchain.chains import ConversationChain
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import SystemMessage
from langchain_core.prompts import PromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, \
    ChatPromptTemplate
from langchain_core.tools import render_text_description_and_args

from tools.eme_task import CreateTask

DEFAULT_SYS_TEMPLATE = """
你是一个应急领域的专家，你需要分析当前的灾情事件信息，按照用户指示协助进行救援活动，如果预案步骤有明显的前后关系，在前一个步骤完成后再生成后一个阶段的任务。

如果想要使用工具话，以JSON格式生成调用数据，不要添加markdown语法标识，不要换行，返回时不要改变字段的顺序（字段顺序很重要）：
Question: 需要你回答的问题
Thought: 你应该时刻思考该做什么 
Action: 要执行的方法，需要是工具列表 [{tool_names}] 中的一个
Action Input: 工具的输入,JSON字符串，不要添加markdown语法标识
Observation: <result>方法执行的结果</result>
... 可能会重复N次
Final Answer: 原始问题的最终答案

可以使用的工具如下：

{tools}

应急预案流程，不要生成预案中不相关的任务，：
第一步：紧急会商，区长组织各应急部门进行会商，判断当前事件等级以及决定采用几级预案响应
第二步：在会商完成后，根据结果，启动对应的预案，开始进行物资调拨、人员调度等工作
第三步：启动预案之后，按需要成立现场指挥部进行现场指挥救援
第四步：救援完成后，进行事后总结

人员组织树：
- 区长：张三
- 街道巡查人员：王五
- 值班员：李四

事件的处理历史：
{intermediate_steps}

Thought:{agent_scratchpad}
"""

sys_prompt = SystemMessagePromptTemplate.from_template(DEFAULT_SYS_TEMPLATE)
human_template = "{input}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt = ChatPromptTemplate.from_messages([sys_prompt, human_template])

tools = [
    CreateTask()
]

# conversation = ConversationChain(llm=ChatOllama(model='qwen2:7b-instruct'), prompt=PROMPT, tools=tools)

# resp = conversation.invoke('发生了一起森林大火，请分析现在的情况，并为相关人员分配任务')
# print(resp)



# ReActSingleInputOutputParser
# ReActOutputParser
agent = create_react_agent(llm=ChatOllama(model='qwen2:7b-instruct'), prompt=chat_prompt, tools=tools,
                           tools_renderer=render_text_description_and_args,
                           output_parser=ReActSingleInputOutputParser(), stop_sequence=['Final Answer', 'Observation'])
# resp = agent.invoke(input={'input': '发生了一起森林大火，请分析现在的情况，并为相关人员分配任务', 'intermediate_steps': '', 'history': ''})
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent, tools=tools, verbose=True, stream_runnable=True, handle_parsing_errors=False
)
resp = agent_executor.invoke(input={'input': '发生了一起森林大火，请分析现在的情况，并为相关人员分配任务'})
print(resp)
