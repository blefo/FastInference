import concurrent.futures

from typing import List, Tuple
from tqdm import tqdm
from .datablock import DataBlock


class DataProcessor:
    def __init__(self, raw_data: List[Tuple[str, str]]) -> None:
        self.raw_data = raw_data
        self.formated_data = self.build_data_chain()

    def build_data_chain(self) -> List[DataBlock]:
        data_chain = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_date = {executor.submit(self.build_data_block, data) for data in self.raw_data}
            for future in tqdm(concurrent.futures.as_completed(future_to_date), total=len(future_to_date), desc=f"Building Data Chain"):
                result = future.result()
                if result.content is not None:
                    data_chain.append(result)

        return data_chain

    @staticmethod
    def build_data_block(data: Tuple[str, str]):
        if data[1] is not None:
            return DataBlock(content=data[0], 
                             metadata={'date_stamp': data[1]})
        else:
            return DataBlock(content=data[0])
