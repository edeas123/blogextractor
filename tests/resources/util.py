import os
from urllib.parse import urlparse
from requests.models import Response
from unittest.mock import Mock

DATA_DIR = '../data'


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
