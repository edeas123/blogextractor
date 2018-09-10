from bs4 import BeautifulSoup
from blogextractor.model import (
    Topic, Page, Forum, User
)
import requests


class ForumPageExtractor:

    def __init__(self, blog, forum, page_number=0):
        self.blog = blog
        self.forum = forum
        self.page_number = page_number

        self.domain_url = 'http://www.{0}.com'.format(
            blog
        )
        self.forum_url = '{0}/{1}'.format(
            self.domain_url,
            forum
        )
        self.page_url = '{0}/{1}'.format(
            self.forum_url,
            page_number
        )

    # request the html page from the page url
    def request_page(self):
        r = requests.get(url=self.page_url)
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

    # parse the html page and return the page data
    def parse_page(self, html_page):

        soup = BeautifulSoup(html_page, "lxml")

        # parse number of pages
        # number_of_pages = int(soup.body.div.div.next_sibling.find_all("b")[1].text)

        # parse topics on current pages
        core = soup.body.find_all("table")[2]
        tds = core.findAll("td")

        topics = []
        page = Page(
            forum=Forum(name=self.forum),
            page_number=self.page_number
        )

        for td in tds:
            a_data = td.find_all("a")

            _id = a_data[0].get("name")
            title = a_data[1].text
            # info['creator'] = a_data[-2].text
            url = "{}{}".format(self.domain_url, a_data[1].get("href"))

            s_spans = td.find("span", {"class": "s"})
            s_spans_b = s_spans.find_all("b")

            users = s_spans.find_all("a")
            if len(users) == 2:  # first and last user is valid
                creator = users[0].text
                comments = int(s_spans_b[1].text)
                views = int(s_spans_b[2].text)
            else:
                creator = None
                comments = int(s_spans_b[0].text)
                views = int(s_spans_b[1].text)

            topics.append(
                Topic(
                    _id=_id,
                    title=title,
                    url=url,
                    creator=User(name=creator),
                    number_of_posts=comments,
                    number_of_views=views
                )
            )
        page.topics = topics

        return page


class NairalandForumPageExtractor(ForumPageExtractor):

    def __init__(self, blog, forum, page_number=0):
        super(
            NairalandForumPageExtractor,
            self
        ).__init__(
            blog=blog,
            forum=forum,
            page_number=page_number
        )

    def extract(
        self
    ):

        # request the page
        html_page = self.request_page()

        # TODO: check for errors
        # by returning the appropriate error code
        # perhaps using abort(code)

        # parse the page
        return self.parse_page(html_page)

