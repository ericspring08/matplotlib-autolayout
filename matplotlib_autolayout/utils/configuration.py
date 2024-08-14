import re
from typing import Union

class AutoLayoutConfig:
    def __init__(self, config: Union[str, dict]):
        if isinstance(config, str):
            self.config_str = config
            self._process_string_config()
        elif isinstance(config, dict):
            self.config_dict = config
            self._process_dict_config()

    def _process_string_config(self):
        self.config_dict = {}
        config_options = self.config_str.split(' ')

        for config_option in config_options:
            # process config option
            config_str_dict = self.get_str_config_dict(config_option)
            if config_str_dict:
                self.config_dict.update(config_str_dict)
            pass

    def _process_dict_config(self):
        pass

    def get_str_config_dict(self, config_str):
        if config_str == "direction-row":
            return {"direction": "row"}
        elif config_str == "direction-column":
            return {"direction": "column"}
        elif re.match(r"^margin-[+-]?(\d*\.)?\d+$\Z", config_str):
            return {"margin": float(config_str.split("-")[-1])}
        elif re.match(r"^count-\d+\Z", config_str):
            return {"count": int(config_str.split("-")[-1])}

    def get_dict_config_dict(self):
        return self.config_dict
