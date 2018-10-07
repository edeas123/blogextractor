from bs4 import BeautifulSoup
from blogextractor.model import (
    User, Comment
)
from blogextractor.util import to_datetime
from blogextractor.extractors.core import Extractor
from datetime import datetime


class NairalandCommentExtractor(Extractor):

    def __init__(self, url):
        super().__init__()
        self.url = url

    # parse the html page and return the data
    def extract(self):

        comments = []
        offset = 0

        # request the page
        page = self.request_page(url=self.url)
        retrieved_on = datetime.utcnow()

        # parse
        soup = BeautifulSoup(page, "lxml")
        posts = soup.find("table", {"summary": "posts"})
        tds = posts.find_all("td")

        for i in range(0, len(tds), 2):

            i -= offset
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
                day = None

            if len(details) > 2:
                year = details[2].text
            else:
                year = None

            # retrieve poster info
            details = tds[i].find_all("a")
            _id = details[0].get("name")

            if len(details) <= 4:
                user = None
            else:
                user = details[-1].text

            # retrieve content info
            links = len(tds[i + 1].find(
                "div", {"class": "narrow"}
            ).find_all("a"))

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

            images = len(tds[i + 1].find_all(
                "img", {"class": "attachmentimage"})
            )

            quoting = False
            quote = tds[i + 1].find(
                "div", {"class": "narrow"}
            ).find("blockquote")

            if quote:
                quoting = True

            post = Comment(
                _id=_id,
                created_by=User(name=user),
                created_on=to_datetime(time, day, year, offset=1),
                number_of_likes=likes,
                number_of_shares=shares,
                requotes=quoting,
                number_of_links=links,
                number_of_images=images,
                retrieved_on=retrieved_on
            )

            comments.append(post)

        return comments
