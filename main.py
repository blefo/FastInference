from config.config import Config
from data_processing.data_processor import DataProcessor
from managers.task_manager import TasksManager
from managers.llm_manager import LLMManager
from utils.data_processing import extract_response_only

import asyncio

async def main():
    config = Config('config.json')
    llm_manager = LLMManager(config)

    task_manager = TasksManager(24)

    data = DataProcessor([("This is a test", {"data_stamp": "2010-01-12"}),
                          ('This is a second test', {"data_stamp": '2013-01-05'})],
                         task_manager)

    data.render_prompt_for_many("This is the context: {content} with value {data_stamp}")

    data.render_prompt_for_many_litellm_format()

    tasks = await task_manager.build_async(llm_manager.acompletion, data.datablock_chain)
    results = await asyncio.gather(*tasks)

    results_only_response = extract_response_only(results, task_manager)

    return results_only_response

if __name__ == '__main__':
    asyncio.run(main())
