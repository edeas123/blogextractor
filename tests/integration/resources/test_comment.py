from tests.integration.resources.core import ResourceTestCase
from tests.integration.resources.core import get_page
from unittest.mock import patch
from blogextractor._version import API_PATH


class NairalandCommentResourceTestCase(ResourceTestCase):

    def setUp(self):
        super().setUp()

        self.url = 'https://www.nairaland.com/4720224/0'
        self.first_comment = {
            'id': 70983044,
            'title': None,
            'created_by': "kahal29",
            'created_on': "2018-09-07T11:44:00+00:00",
            'number_of_likes': 2,
            'number_of_shares': 0,
            'requotes': False,
            'number_of_links': 2,
            'number_of_images': 2,
            'number_of_words': None
        }
        self.last_comment = {
            'id': 70986722,
            'title': None,
            'created_by': "Shampoo77",
            'created_on': "2018-09-07T13:49:00+00:00",
            'number_of_likes': 0,
            'number_of_shares': 0,
            'requotes': False,
            'number_of_links': 0,
            'number_of_images': 0,
            'number_of_words': None
        }

    @patch('requests.get')
    def test_extract(self, mock_get):

        # mock out returning the web page
        mock_get.return_value = get_page(self.url)

        with self.app.test_client() as c:
            resp = c.get(
                f'{API_PATH}/comment?url={self.url}'
            )

            # assert that you got a 200 status code
            self.assertEqual(resp.status_code, 200)

            # load the resp text into json and assert content
            resp_json = resp.json['data']

            resp_json[0]['created_on'] = "2018-09-07T11:44:00+00:00"
            resp_json[-1]['created_on'] = "2018-09-07T13:49:00+00:00"

            del resp_json[0]['retrieved_on']
            del resp_json[-1]['retrieved_on']

            self.assertEqual(resp_json[0], self.first_comment)
            self.assertEqual(resp_json[-1], self.last_comment)
