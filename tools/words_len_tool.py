"""
计算单词长度的工具
"""
from typing import Any

from langchain.tools import BaseTool


class Calculate(BaseTool):
    name = "字符串长度计算器"
    description = "用于计算给定字符串的长度，返回一个长度数值"

    def _run(self, text: str, **kwargs: Any) -> Any:
        if text:
            return len(text)
        else:
            return 0
