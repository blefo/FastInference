from config.config import Config
from data_processing.data_processor import DataProcessor
from managers.task_manager import TasksManager
from prompt.prompt_template import PromptTemplate

from litellm import acompletion
import asyncio

if __name__ == '__main__':
    conf = Config('config.json')
    print(conf)

    data = DataProcessor([("This is a test", "2010-01-12"),
                          ('This is a second test', '2013-01-05')])

    task_manager = TasksManager(24)

    prompt = PromptTemplate({'variable1': 'context is a string', 'variable2': 12},
                            "This is the context: {variable1} with value {variable2}")



    print(prompt)

    async def test_get_response():
        user_message = "Hello, how are you?"
        messages = [{"content": user_message, "role": "user"}]
        response = await acompletion(model="huggingface/mistralai/Mistral-7B-Instruct-v0.2", 
                                     messages=messages, 
                                     api_key="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")
        return response

    response = asyncio.run(test_get_response())
    print(response)
