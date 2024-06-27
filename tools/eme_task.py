from typing import Any, Type, Dict

from langchain_core.tools import tool, StructuredTool
from pydantic import BaseModel, Field


class CalculatorInput(BaseModel):
    assignee: str = Field(description="任务处理人")
    task_desc: str = Field(description="任务详情")


class CreateTask(StructuredTool):
    name = "create_eme_task"

    description = "用于创建应急任务"
    args_schema: Type[BaseModel] = CalculatorInput

    def _run(self, task_desc: str = None, assignee: str = None, **kwargs: Any) -> Any:
        print('创建任务 ' + task_desc)
        return True
