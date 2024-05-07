from data_processing.datablock import DataBlock
from managers.task_manager import TasksManager

from typing import List


def extract_response_only(data: List, task_manager: TasksManager) -> List:
    def get_response(response):
        return response.choices[0].message.content

    return task_manager.build_multithread(get_response, data, "Building the LLM Response only")
