from bs4 import BeautifulSoup
from blogextractor.model import (
    Post, User
)
from blogextractor.util import to_datetime
import requests


class PostExtractor:

    def __init__(self, blog, topic_id, page_number=0):
        self.blog = blog
        self.topic_id = topic_id
        self.page_number = page_number

        self.domain_url = 'http://www.{0}.com'.format(
            blog
        )
        self.page_url = '{0}/{1}'.format(
            self.domain_url,
            self.topic_id,
            page_number
        )

    def request_page(self):
        r = requests.get(url=self.page_url)
        if r.status_code != 200:
            print(
                "{0}: {1}".format(
                    r.status_code,
                    r.reason
                )
            )
            return None
        return r.text

    def parse_post(self, page):

        """
        Parse_article => uses request to retrieve first page
            of article, and uses soup to extract content of the page..
        """

        comments = []
        offset = 0

        # parse
        soup = BeautifulSoup(page, "lxml")
        posts = soup.find("table", {"summary": "posts"})
        tds = posts.find_all("td")

        for i in range(0, len(tds), 2):
            comment = {}
            i -= offset
            # print i,
            # retrieve timestamp info
            #        print tds[i]
            details = tds[i].find("span", {"class": "s"})
            if details:
                details = details.find_all("b")
            else:
                # print "bug",
                offset += 1
                continue

            time = details[0].text
            if len(details) > 1:
                day = details[1].text
            else:
                day = "July 17"

            if len(details) > 2:
                year = details[2].text
            else:
                year = "2017"

            # retrieve poster info
            details = tds[i].find_all("a")
            _id = details[0].get("name")

            if len(details) <= 4:
                user = None
            else:
                user = details[-1].text

            # retrieve content info
            links = len(tds[i + 1].find("div", {"class": "narrow"}).find_all("a"))
            likes = tds[i + 1].find("p", {"class": "s"})
            if likes:
                likes = likes.find_all("b")[0].text.strip()

            if not likes:
                likes = 0
            else:
                likes = int(likes.split()[0])

            shares = tds[i + 1].find("p", {"class": "s"})
            if shares:
                shares = shares.find_all("b")[1].text.strip()

            if not shares:
                shares = 0
            else:
                shares = int(shares.split()[0])

            images = len(tds[i + 1].find_all("img", {"class": "attachmentimage"}))

            quoting = False
            quote = tds[i + 1].find("div", {"class": "narrow"}).find("blockquote")
            if quote:
                quoting = True

            post = Post(
                _id=_id,
                user=User(name=user),
                ts=to_datetime(time, day, year),
                number_of_likes=likes,
                number_of_shares=shares,
                requotes=quoting,
                number_of_links=links,
                number_of_images=images
            )

            comments.append(post)

        return comments


class NairalandPostExtractor(PostExtractor):

    def __init__(self, blog, topic_id, page_number=0):
        super(
            NairalandPostExtractor,
            self
        ).__init__(
            blog=blog,
            topic_id=topic_id,
            page_number=page_number
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
        return self.parse_post(html)