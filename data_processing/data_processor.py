from typing import Tuple, Dict, List
from prompt.prompt_template import PromptTemplate
from data_processing.datablock import DataBlock
from managers.task_manager import TasksManager


class DataProcessor:
    def __init__(self, raw_data: List[Tuple[str, Dict]], task_manager: TasksManager) -> None:
        self.raw_data = raw_data
        self.task_manager = task_manager
        self.datablock_chain = self.build_data_chain()

    def build_data_chain(self) -> List[DataBlock]:
        return self.task_manager.build_multithread(self.build_data_block, self.raw_data, "Building Data Chain")

    @staticmethod
    def build_data_block(data: Tuple[str, Dict]):
        if data[1] is not None:
            return DataBlock(content=data[0],
                             metadata=data[1])
        else:
            return DataBlock(content=data[0])

    @staticmethod
    def build_prompt_in_datablock(data: DataBlock, prompt_core: str) -> DataBlock:
        prompt = PromptTemplate(data, prompt_core)
        data.__setattr__('prompt_with_content', prompt)
        return data

    @staticmethod
    def build_litellm_prompt_in_datablock(data: DataBlock) -> DataBlock:
        try:
            litellm_prompt = data.prompt_with_content.render_prompt_for_litellm()
        except Exception as e:
            raise Exception('Could not get the prompt_with_content attribute in the PromptTemplate class: ', e)
        data.__setattr__('litellm_prompt_object', litellm_prompt)
        return data

    def render_prompt_for_many(self, prompt_core: str) -> None:
        try:
            self.task_manager.build_multithread(self.build_prompt_in_datablock, self.datablock_chain,
                                                task_name="Building Prompt in DataChain", prompt_core=prompt_core)
        except Exception as e:
            raise Exception('Could not build the PromptTemplate in the DataBlock object: ', e)

    def render_prompt_for_many_litellm_format(self) -> None:
        try:
            self.task_manager.build_multithread(self.build_litellm_prompt_in_datablock, self.datablock_chain,
                                                task_name="Building LiteLLM object in DataBlockChain")
        except Exception as e:
            raise Exception('Could not build the LiteLLM prompt format in the DataBlockChain: ', e)
