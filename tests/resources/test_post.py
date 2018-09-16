from tests.resources.core import ResourceTestCase
from tests.resources.util import get_page
from unittest.mock import patch


class NairalandPostResourceTestCase(ResourceTestCase):

    def setUp(self):
        super().setUp()

        self.blog = 'nairaland'
        self.topic_id = 4720224
        self.page = 0
        self.url = 'https://www.{0}.com/{1}/{2}'.format(
            self.blog,
            self.topic_id,
            self.page
        )
        self.expected0 = {
            'id': 70983044,
            'title': None,
            'user': "kahal29",
            'ts': "2018-09-07T11:44:00+00:00",
            'number_of_likes': 2,
            'number_of_shares': 0,
            'requotes': False,
            'number_of_links': 2,
            'number_of_images': 2,
            'retrieved_on': None
        }

    @patch('requests.get')
    def test_extract(self, mock_get):

        # mock out returning the web page
        mock_get.return_value = get_page(self.url)

        with self.app.test_client() as c:
            resp = c.get(
                'api/v1/post/?blog={0}'
                '&id={1}&page_number={2}'.format(
                    self.blog,
                    self.topic_id,
                    self.page
                )
            )

            # assert that you got a 200 status code
            self.assertEqual(resp.status_code, 200)

            # load the resp text into json and assert content
            resp_json = resp.json
            self.assertEqual(resp_json[0], self.expected0)
