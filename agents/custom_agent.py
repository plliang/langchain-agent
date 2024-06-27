from langchain.agents import Tool, AgentExecutor, BaseSingleActionAgent
from langchain_community.llms import Ollama

from typing import List, Tuple, Any, Union

from langchain.agents import AgentExecutor, BaseSingleActionAgent
from langchain.schema import AgentAction, AgentFinish

search = Ollama(model='qwen2:7b-instruct')
tools = [
    Tool(
        name="createEventTask",
        func=search.invoke,
        description="创建应急事件任务的方法",
        return_direct=True,
    )
]


class FakeAgent(BaseSingleActionAgent):
    """虚拟自定义代理。"""

    @property
    def input_keys(self):
        return ["input"]

    def plan(
            self, intermediate_steps: List[Tuple[AgentAction, str]], **kwargs: Any
    ) -> Union[AgentAction, AgentFinish]:
        """根据输入决定要做什么。

        Args:
            intermediate_steps: LLM到目前为止采取的步骤以及观察结果
            **kwargs: 用户输入

        Returns:
            指定要使用的工具的行动。
        """
        return AgentAction(tool="createEventTask", tool_input=kwargs["input"], log="")

    async def aplan(
            self, intermediate_steps: List[Tuple[AgentAction, str]], **kwargs: Any
    ) -> Union[AgentAction, AgentFinish]:
        """根据输入决定要做什么。

        Args:
            intermediate_steps: LLM到目前为止采取的步骤以及观察结果
            **kwargs: 用户输入

        Returns:
            指定要使用的工具的行动。
        """
        return AgentAction(tool="createEventTask", tool_input=kwargs["input"], log="")


agent = FakeAgent()
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent, tools=tools, verbose=True, stream=True
)
print(agent_executor.invoke("你作为一个应急领域专家，有权限使用以下工具来完成任务:\n\n            create_eme_task - 用于创建应急任务, args: {'assignee': {'description': '任务处理人', 'title': 'Assignee', 'type': 'string'}, 'task_desc': {'description': '任务详情', 'title': 'Task Desc', 'type': 'string'}}\n\n            如果要调用工具的话，使用如下格式：\n            Question: 需要你回答的问题\n            Thought: 你应该时刻思考该做什么 \n            Action: 要执行的方法，需要是工具列表 [字符串长度计算器, create_eme_task] 中的一个\n            Action Input: 要执行方法的参数，你需要给一个完整的JSON类型参数\n            Observation: 方法执行的结果\n            ... 可能会重复N次\n            Final Answer: 原始问题的最终答案\n            \n            开始\n            Question: 给张三创建一个应急任务，让他去采购一些应急物资\n            Thought:"))
