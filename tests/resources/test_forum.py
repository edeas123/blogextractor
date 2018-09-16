from tests.resources.core import ResourcesTestCase
from unittest.mock import patch
from tests.resources.util import get_page


class NairalandForumResourceTestCase(ResourcesTestCase):

    def setUp(self):
        super().setUp()

        self.blog = 'nairaland'
        self.forum = 'politics'
        self.url = 'http://www.{0}.com/{1}'.format(
            self.blog,
            self.forum
        )
        self.expected = {
            'name': self.forum,
            'ad_rate': None,
            'ad_period': None,
            'percent_discount': None,
            'sub_forums': None,
            'number_of_pages': 8517,
            'forum_pages': None,
            'retrieved_on': None
        }

    @patch('requests.get')
    def test_extract(self, mock_get):

        # mock out returning the web page
        mock_get.return_value = get_page(self.url)

        with self.app.test_client() as c:
            resp = c.get(
                'api/v1/forum/?blog={0}'
                '&forum={1}'.format(
                    self.blog,
                    self.forum
                )
            )

            # assert that you got a 200 status code
            self.assertEqual(resp.status_code, 200)

            # load the resp text into json and assert content
            resp_json = resp.json
            self.assertEqual(resp_json, self.expected)
