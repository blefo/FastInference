from config.config import Config
from data_processing.data_processor import DataProcessor
from managers.task_manager import TasksManager
from managers.llm_manager import LLMManager
from utils.data_processing import extract_response_only, extract_from_file

import asyncio

async def main():
    config = Config('config.json')
    llm_manager = LLMManager(config)

    task_manager = TasksManager(24)

    data_load = extract_from_file("xlsx",
                                  r"C:\Users\baptiste.lefort\Documents\final_results\perimeter_headlines.xlsx",
                                  "Title",
                                  task_manager)[:20]

    data = DataProcessor(data_load,
                         task_manager)

    data.render_prompt_for_many("This is the context: {content} with value {Date}")

    data.render_prompt_for_many_litellm_format()

    tasks = await task_manager.build_async(llm_manager.acompletion, data.datablock_chain)
    results = await asyncio.gather(*tasks)

    results_only_response = extract_response_only(results, task_manager)

    return results_only_response

if __name__ == '__main__':
    asyncio.run(main())
