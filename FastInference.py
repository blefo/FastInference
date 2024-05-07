from config.config import Config
from managers.llm_manager import LLMManager
from managers.task_manager import TasksManager
from data_processing.data_processor import DataProcessor
from utils.data_processing import extract_from_file, extract_response_only

import asyncio


class FastInference:
    def __init__(self, file_path: str, main_column: str, prompt: str, only_response: bool = True):
        self.config = Config('config.json')
        self.llm_manager = LLMManager(self.config)
        self.task_manager = TasksManager()
        self.file_path = file_path
        self.main_column = main_column
        self.prompt = prompt
        self.only_response = only_response

    def run(self):
        return asyncio.run(self.run_process())

    async def run_process(self):
        # Build the DataBlockChain
        data_loaded = extract_from_file(self.file_path,
                                        self.main_column,
                                        self.task_manager)[:20]

        data = DataProcessor(data_loaded, self.task_manager)
        data.render_prompt_for_many(self.prompt)
        data.render_prompt_for_many_litellm_format()

        # Run the LLM
        tasks = await self.task_manager.build_async(self.llm_manager.acompletion, data.datablock_chain)
        results = await asyncio.gather(*tasks)

        if self.only_response:
            return extract_response_only(results, self.task_manager)
        else:
            return results