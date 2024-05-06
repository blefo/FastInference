from dataclasses import dataclass


@dataclass
class DataBlock:
    def __init__(self, content: str, metadata: dict = {}) -> None:
        self.content = content
        self.metadata = metadata
    
    def is_time_series(self) -> bool:
        if 'date_stamp' in self.metadata:
            return True
        else:
            return False