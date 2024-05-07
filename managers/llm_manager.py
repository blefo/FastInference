class LLMManager:
    def __init__(self, config) -> None:
        self.model_name = config.model_name
        self.api_key = config.api_key
        self.custom_llm_provider = config.custom_llm_provider


    # async def acompletion(self, ):
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
        
