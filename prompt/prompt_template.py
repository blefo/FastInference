from typing import Dict


class PromptTemplate:
    def __init__(self, variables: Dict[str, any], core_prompt: str):
        self.variables = variables
        self.core_prompt = core_prompt
        self.prompt = self.render_prompt()

    def render_prompt(self):
        try:
            return self.core_prompt.format(**self.variables)
        except Exception as e:
            raise Exception(f"Missing variable '{e}' in the prompt template.")