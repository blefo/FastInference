import asyncio
import concurrent.futures
from tqdm import tqdm
from typing import List

from data_processing.datablock import DataBlock


class TasksManager:
    def __init__(self, nb_thread: int = None) -> None:
        self.nb_thread = nb_thread

    def build(self, function_to_execute: object, data: List[DataBlock]) -> List:
        tasks = []

        with concurrent.futures.ThreadPoolExecutor(self.nb_thread) as executor:
            future_to_date = {executor.submit(function_to_execute, content) for content in data}
            for future in tqdm(concurrent.futures.as_completed(future_to_date), total=len(future_to_date), desc=f"Building Tasks List"):
                result = future.result()
                if result is not None:
                    tasks.append(result)

        return tasks