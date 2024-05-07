import asyncio

from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial

from tqdm import tqdm
from typing import List, Callable

from data_processing.datablock import DataBlock


class TasksManager:
    def __init__(self, nb_thread: int = None) -> None:
        self.nb_thread = nb_thread

    def build(self, function_to_execute: Callable, data: list, task_name: str, **kwargs) -> List:
        tasks = []

        func_with_kwargs = partial(function_to_execute, **kwargs)
        with ThreadPoolExecutor(self.nb_thread) as executor:
            future_to_date = {executor.submit(func_with_kwargs, content) for content in data}
            for future in tqdm(as_completed(future_to_date), total=len(future_to_date), desc=task_name):
                result = future.result()
                if result is not None:
                    tasks.append(result)

        return tasks