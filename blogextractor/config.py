import os
import yaml


class Config(object):

    def __init__(self, config):
        for k, v in config.items():
            setattr(self, k, v)

    # defines the default config fields
    PORT = 5000


# get the project root directory
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# define the default config file
CONFIG_FILE_NAME = "environment_{}.yml".format(
    os.environ.get('APP_ENVIRONMENT', 'local')
)
DEFAULT_CONFIG_FILE = os.path.join(PROJECT_DIR, CONFIG_FILE_NAME)


def load_config(config_file=DEFAULT_CONFIG_FILE):
    with open(config_file, 'r') as yml_file:
        config = Config(yaml.load(yml_file))

    return config
