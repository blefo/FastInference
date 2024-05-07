import backoff
import requests
import aiohttp

from litellm import acompletion
from typing import List, Dict

from prompt.prompt_template import PromptTemplate


class LLMManager:
    def __init__(self, config) -> None:
        self.model_name = config.model_name
        self.api_key = config.api_key

    @backoff.on_exception(backoff.expo,
                          (requests.exceptions.Timeout,
                           requests.exceptions.RequestException,
                           aiohttp.ClientResponseError),
                          max_time=300)
    async def acompletions_with_backoff(self, **kwargs):
        return await acompletion(**kwargs)

    async def acompletion(self, content: List[Dict]):
        return await self.acompletions_with_backoff(model=self.model_name,
                                                    messages=content,
                                                    api_key=self.api_key)

    #
    #
    # async def test_get_response():
    #     user_message = "Hello, how are you?"
    #     messages = [{"content": user_message, "role": "user"}]
    #     response = await acompletion(model="huggingface/mistralai/Mistral-7B-Instruct-v0.2",
    #                                  messages=messages,
    #                                  api_key="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")
    #     return response
    #
    # response = asyncio.run(test_get_response())
        
