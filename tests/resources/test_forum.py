from tests.resources.core import ResourceTestCase
from unittest.mock import patch
from tests.util import get_page


class NairalandForumResourceTestCase(ResourceTestCase):

    def setUp(self):
        super().setUp()

        self.url = 'https://www.nairaland.com/politics/8625'
        self.viewers = [{}]
        self.expected = {
            'name': None,
            'url': self.url,
            'ad_rate': None,
            'ad_period': None,
            'percent_discount': None,
            'sub_forums': None,
            'number_of_pages': 8626,
            'page_number': None,
            'viewers': self.viewers,
            'number_of_guests': None
        }
        self.first_topic = {
            'id': '3463',
            'title': ' Between Six and Half A- Dozen- [Poem for Nigeria]',
            'url': '/3463/between-six-half-dozen-poem',
            'rank': None,
            'number_of_posts': 1,
            'number_of_views': 1251,
            'creator': 'conscience',
            'last_comment_by': 'conscience',
            'last_comment_at': None,
            'number_of_pages': None
        }
        self.last_topic = {
            'id': '2036',
            'title': 'Pictures On the New 1,000 Naira Note',
            'url': '/2036/pictures-new-1000-naira-note',
            'rank': None,
            'number_of_posts': 85,
            'number_of_views': 17747,
            'creator': 'skima',
            'last_comment_by': 'Seun',
            'last_comment_at': None,
            'number_of_pages': None
        }

    @patch('requests.get')
    def test_extract(self, mock_get):

        # mock out returning the web page
        mock_get.return_value = get_page(self.url)

        with self.app.test_client() as c:
            resp = c.get(
                'api/v1/forum/?url={0}'.format(
                    self.url
                )
            )

            # assert that you got a 200 status code
            self.assertEqual(resp.status_code, 200)

            # load the resp text data into json and assert content
            resp_json = resp.json['data']

            # assert the first and last topics are as expected
            del resp_json['topics'][0]['retrieved_on']
            del resp_json['topics'][-1]['retrieved_on']

            self.assertEqual(resp_json['topics'][0], self.first_topic)
            self.assertEqual(resp_json['topics'][-1], self.last_topic)

            del resp_json['topics']
            del resp_json['retrieved_on']

            # assert the forum object is as expected
            self.assertEqual(resp_json, self.expected)
