from config.config import Config
from data_processing.data_processor import DataProcessor
from managers.task_manager import TasksManager

from litellm import acompletion
import asyncio

if __name__ == '__main__':
    conf = Config('config.json')
    print(conf)

    task_manager = TasksManager(24)

    data = DataProcessor([("This is a test", {"data_stamp": "2010-01-12"}),
                          ('This is a second test', {"data_stamp": '2013-01-05'})],
                         task_manager)

    data.render_prompt_for_many("This is the context: {content} with value {data_stamp}")

    data.render_prompt_for_many_litellm_format()

    print("Done")

    async def test_get_response():
        user_message = "Hello, how are you?"
        messages = [{"content": user_message, "role": "user"}]
        response = await acompletion(model="huggingface/mistralai/Mistral-7B-Instruct-v0.2", 
                                     messages=messages, 
                                     api_key="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")
        return response

    response = asyncio.run(test_get_response())
    print(response)
