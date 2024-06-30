from typing import Any, Type, Dict, Union

from langchain_core.tools import tool, StructuredTool
from pydantic import BaseModel, Field


class CalculatorInput(BaseModel):
    assignee: Union[str, dict] = Field(description="任务处理人")
    task_desc: Union[str, dict] = Field(description="任务详情")


class CreateTask(StructuredTool):
    name = "create_eme_task"

    description = "用于创建应急任务"
    args_schema: Type[BaseModel] = CalculatorInput

    def _run(self, assignee: Union[str, dict], task_desc: Union[str, dict] , **kwargs: Any) -> Any:
        print('创建任务 ' + task_desc.__str__() + ',处理人 ' + assignee.__str__())
        return True
