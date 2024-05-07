import backoff
import requests
import aiohttp
import openai

from litellm import acompletion
from typing import List, Dict


class LLMManager:
    def __init__(self, config) -> None:
        self.model_name = config.model_name
        self.api_key = config.api_key

    @backoff.on_exception(backoff.expo,
                          (openai.APITimeoutError,
                           openai.BadRequestError,
                           openai.AuthenticationError,
                           openai.PermissionDeniedError,
                           openai.NotFoundError,
                           openai.UnprocessableEntityError,
                           openai.RateLimitError),
                          max_time=300)
    async def acompletions_with_backoff(self, **kwargs):
        return await acompletion(**kwargs)

    async def acompletion(self, content: List[Dict]):
        return await self.acompletions_with_backoff(model=self.model_name,
                                                    messages=content,
                                                    api_key=self.api_key)
        
