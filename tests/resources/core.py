import unittest

from blogextractor.api_main import create_app
from blogextractor.config import load_config


class ResourcesTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        config = load_config()
        cls.app = create_app(config=config)