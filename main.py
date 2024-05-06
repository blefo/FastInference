from config.config import Config

if __name__ == '__main__':
    conf = Config('config.json')
    print(conf)

    from litellm import acompletion
    import asyncio

    async def test_get_response():
        user_message = "Hello, how are you?"
        messages = [{"content": user_message, "role": "user"}]
        response = await acompletion(model="huggingface/mistralai/Mistral-7B-Instruct-v0.2", 
                                     messages=messages, 
                                     api_key="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")
        return response

    response = asyncio.run(test_get_response())
    print(response)
