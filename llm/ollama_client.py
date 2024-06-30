from langchain_community.llms import Ollama

"""
提供基于ollama的模型服务基础服务功能
"""


class OllamaClient:


    def invoke(self, model: str, messages: str):
        llm = Ollama(model=model)

        response = llm.invoke(messages)
        return response


client = OllamaClient()
# LLMChain(llm=Ollama('qwen2:7b-instruct'), )
resp = client.invoke('qwen2:7b-instruct', "你作为一个应急领域专家，有权限使用以下工具来完成任务:\n\n            create_eme_task - 用于创建应急任务, args: {'assignee': {'description': '任务处理人', 'title': 'Assignee', 'type': 'string'}, 'task_desc': {'description': '任务详情', 'title': 'Task Desc', 'type': 'string'}}\n\n            如果要调用工具的话，使用如下格式：\n            Question: 需要你回答的问题\n            Thought: 你应该时刻思考该做什么 \n            Action: 要执行的方法，需要是工具列表 [字符串长度计算器, create_eme_task] 中的一个\n            Action Input: 要执行方法的参数，你需要给一个完整的JSON类型参数\n            Observation: 方法执行的结果\n            ... 可能会重复N次\n            Final Answer: 原始问题的最终答案\n            \n            开始\n            Question: 给张三创建一个应急任务，让他去采购一些应急物资\n            Thought:")
print(resp)

