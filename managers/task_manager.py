import asyncio
import concurrent.futures
from tqdm import tqdm
from typing import List


class TasksManager:
    def __init__(self, is_time_series: bool, nb_thread: int = None) -> None:
        self.nb_thread = nb_thread
        self.is_time_series = is_time_series

    def build(self, function_to_execute: object, data: List[str]) -> List:
        tasks = []

        with concurrent.futures.ThreadPoolExecutor(self.nb_thread) as executor:
            future_to_date = {executor.submit(function_to_execute, content) for content in data}
            for future in tqdm(concurrent.futures.as_completed(future_to_date), total=len(future_to_date), desc=f"Building Tasks"):
                result = future.result()
                if result is not None:
                    tasks.append(result)

        return tasks