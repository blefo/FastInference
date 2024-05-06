class LLMManager:
    def __init__(self, config) -> None:
        self.model_name = config.model_name
        self.api_key = config.api_key
        self.custom_llm_provider = config.custom_llm_provider
        
