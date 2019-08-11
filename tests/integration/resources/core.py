import unittest
import os

from urllib.parse import urlparse
from requests.models import Response
from unittest.mock import Mock

from blogextractor.api_main import create_app
from blogextractor.config import load_config

DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data'
)


class ResourceTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        config = load_config()
        cls.app = create_app(config=config)


def get_page(url):
    p_url = urlparse(url)
    filename = os.path.join(
        DATA_DIR,
        '{0}{1}.htm'.format(
            p_url.netloc.replace('.', ''),
            p_url.path.replace('/', '')
        )
    )

    with open(filename, 'r', encoding='utf-8') as page:
        text = page.read()

        page_response = Mock(spec=Response)
        page_response.text = text
        page_response.status_code = 200

        return page_response
