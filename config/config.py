import json


class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = {}
        self.load_config()

    def __getattr__(self, item):
        try:
            return self.config[item]
        except KeyError:
            raise AttributeError(f"{self.__class__.__name__} has no attribute '{item}'")

    def load_config(self):
        if self.config_file is None:
            print('The configuration JSON file does not exist or is empty.')
            return None
        try:
            with open(self.config_file, "r") as f:
                config = json.load(f)
            for key, value in config.items():
                self.__dict__[key] = value
                setattr(self, key, value)
            return self.__dict__
        except Exception as e:
            print('Error when getting configuration: ', e)
