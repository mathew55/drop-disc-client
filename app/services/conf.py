from pyhocon import ConfigFactory
from pathlib import Path
from app.services.utils import get_project_root

# A simple class to encapsulate reading of model config variables
class Config:
    _configFile = "conf/application.conf"
    _configs = None
    _instance = None

    def __init__(self):
        if self._instance is None:
            self._instance = super(Config, self).__init__()
            _conf_file = Path.joinpath(get_project_root(), self._configFile)
            self._configs = ConfigFactory.parse_file(_conf_file)

    def get_config_value(self, key_name, xpath=""):
        if xpath == "":
            return self._configs.get_config(key_name)
        else:
            return self._configs.get_config(key_name)[xpath]