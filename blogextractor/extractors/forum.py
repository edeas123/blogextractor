from bs4 import BeautifulSoup
from blogextractor.model import Forum
import requests


class ForumExtractor(object):

    def __init__(self, blog, forum):
        self.blog = blog
        self.forum = forum

        self.domain_url = 'http://www.{0}.com'.format(
            blog
        )
        self.forum_url = '{0}/{1}'.format(
            self.domain_url,
            forum
        )

    # request the html page from the page url
    def request_page(self):
        r = requests.get(url=self.forum_url)
        if r.status_code != 200:
            print(
                "{0}: {1}".format(
                    r.status_code,
                    r.reason
                )
            )
            # TODO: return an appropriate message
            return None

        return r.text

    # parse the html page and return the forum data
    def parse_forum(self, html):

        soup = BeautifulSoup(html, "lxml")

        # parse number of pages
        number_of_pages = int(
            soup.body.div.div.next_sibling.find_all("b")[1].text
        )

        forum = Forum(
            name=self.forum,
            number_of_pages=number_of_pages
        )

        return forum


class NairalandForumExtractor(ForumExtractor):

    def __init__(self, blog, forum):
        super(
            NairalandForumExtractor,
            self
        ).__init__(
            blog=blog,
            forum=forum
        )

    def extract(
        self
    ):
        # request the page
        html = self.request_page()

        # TODO: check for errors
        # by returning the appropriate error code
        # perhaps using abort(code)

        # parse the page
        return self.parse_forum(html)
