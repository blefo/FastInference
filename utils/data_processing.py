from managers.task_manager import TasksManager

from typing import List, Tuple, Dict
from itertools import chain

import pandas as pd
import numpy as np


def extract_response_only(data: List, task_manager: TasksManager) -> List:
    def get_response(response):
        return response.choices[0].message.content

    return task_manager.build_multithread(get_response, data, "Building the LLM Response only")


def extract_from_file(file_type: str,
                      path: str,
                     column_main_content: str,
                     task_manager: TasksManager,
                     nb_chunks: int = 20) -> List[Tuple[str, Dict]]:
    def extract_chunks(data_chunk: pd.DataFrame, column_main_content: str) -> List[Tuple[str, Dict]]:
        result = []

        for index, row in data_chunk.iterrows():
            main_content = row[column_main_content]
            other_data = {col: row[col] for col in data_chunk.columns if col != column_main_content}
            result.append((main_content, other_data))

        return result

    if file_type == "csv":
        data = pd.read_csv(path)
    elif file_type == "xlsx":
        data = pd.read_excel(path)

    data_chunks = np.array_split(data, nb_chunks)

    list_formatted: List = task_manager.build_multithread(extract_chunks,
                                          data_chunks,
                                          f"Formating the {file_type} file",
                                          column_main_content=column_main_content)
    list_flatten = list(chain.from_iterable(list_formatted))

    return list_flatten

