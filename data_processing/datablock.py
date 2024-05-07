from dataclasses import dataclass


@dataclass
class DataBlock:
    content: str
    metadata: dict = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}

    def is_time_series(self) -> bool:
        return 'date_stamp' in self.metadata
