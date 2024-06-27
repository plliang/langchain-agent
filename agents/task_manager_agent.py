"""
管理智能体，作为总体任务的接入，用于生成任务并调用其它Agent或者Function完成任务
"""

from typing import List

system_prompt = "你作为一个应急领域专家，有权限使用以下工具来完成任务:\n\n            字符串长度计算器 - 用于计算给定字符串的长度，返回一个长度数值, args: {'text': {'title': 'Text', 'type': 'string'}, 'kwargs': {'title': 'Kwargs', 'type': 'object'}}\ncreate_eme_task - 用于创建应急任务, args: {'assignee': {'description': '任务处理人', 'title': 'Assignee', 'type': 'string'}, 'task_desc': {'description': '任务详情', 'title': 'Task Desc', 'type': 'string'}}\n\n            如果要调用工具的话，使用如下格式：\n            Question: 需要你回答的问题\n            Thought: 你应该时刻思考该做什么 \n            Action: 要执行的方法，需要是工具列表 [字符串长度计算器, create_eme_task] 中的一个\n            Action Input: 要执行方法的参数，你需要给一个完整的JSON类型参数\n            Observation: 方法执行的结果\n            ... 可能会重复N次\n            Final Answer: 原始问题的最终答案\n            \n            开始\n            Question: 给张三创建一个应急任务，让他去采购一些应急物资\n            Thought:\n            "


class Manager:

    """
    @:param agents
    @:param function_list 允许agent调用的方法列表
    """
    def __init__(self, agents: List, function_list: List):
        self.function_list_prompt = None

    def agent_init(self, agents: List):


    def function_init(self, function_list):

        if function_list:
            self.function_list_prompt = ''
            for function in function_list:
                self.function_list_prompt += function

    def call(self):
        return 'ok'
