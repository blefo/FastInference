from typing import List, Dict
from data_processing.datablock import DataBlock


class PromptTemplate:
    def __init__(self, data: DataBlock, core_prompt: str):
        self.data = data
        self.core_prompt = core_prompt
        self.prompt = self.render_prompt()

    def render_prompt(self) -> str:
        try:
            format_dict = {'content': self.data.content, **self.data.metadata}
            return self.core_prompt.format(**format_dict)
        except KeyError as e:
            raise ValueError(f"Missing variable {e} in the prompt template.")

    def render_prompt_for_litellm(self) -> List[Dict]:
        try:
            return [{"content": self.prompt, "role": "user"}]
        except Exception as e:
            print(f'Could not convert the prompt in the litellm format: {e}')