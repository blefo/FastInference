import backoff
import openai

from litellm import acompletion
from typing import List, Dict


class LLMManager:
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)

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
        return await acompletion(**self.__dict__, **kwargs)

    async def acompletion(self, content: List[Dict]):
        return await self.acompletions_with_backoff(messages=content)
        
