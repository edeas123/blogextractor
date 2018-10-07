from bs4 import BeautifulSoup
from blogextractor.model import Forum, Topic, User
from blogextractor.extractors.core import Extractor


class NairalandForumExtractor(Extractor):

    def __init__(self, url):
        super().__init__()
        self.url = url

    # parse the html page and return the forum data
    def extract(self) -> Forum:

        # request the page
        html = self.request_page(url=self.url)

        # parse the page
        soup = BeautifulSoup(html, "lxml")

        # parse for number of pages
        pages = soup.body.div.div.next_sibling.find_all("b")
        if len(pages) <= 1:
            return Forum()

        number_of_pages = int(
            pages[1].text
        )

        # parse topics on current pages
        core = soup.body.find_all("table")[2]
        tds = core.findAll("td")

        topics = []
        for td in tds:
            a_data = td.find_all("a")

            _id = a_data[0].get("name")
            title = a_data[1].text
            topic_url = "{}{}".format("", a_data[1].get("href"))

            s_spans = td.find("span", {"class": "s"})
            s_spans_b = s_spans.find_all("b")

            users = s_spans.find_all("a")
            if len(users) == 2:
                # first and last user is valid
                creator = users[0].text
                last_comment_by = users[1].text
                comments = int(s_spans_b[1].text)
                views = int(s_spans_b[2].text)
            else:
                creator = None
                last_comment_by = None
                s_spans_a_b = s_spans_b[0].find_all("a")
                if len(s_spans_a_b) > 0:
                    # the first user is valid
                    creator = s_spans_a_b[0].text
                    comments = int(s_spans_b[1].text)
                    views = int(s_spans_b[2].text)
                else:
                    comments = int(s_spans_b[0].text)
                    views = int(s_spans_b[1].text)

                s_spans_a_b = s_spans_b[-1].find_all("a")
                if len(s_spans_a_b) > 0:
                    # the last user is valid
                    last_comment_by = s_spans_a_b[0].text

            topics.append(
                Topic(
                    _id=_id,
                    title=title,
                    url=topic_url,
                    creator=User(name=creator),
                    number_of_posts=comments,
                    number_of_views=views,
                    last_comment_by=User(name=last_comment_by)
                )
            )

        # build Forum object
        forum = Forum(
            url=self.url,
            number_of_pages=number_of_pages,
            topics=topics
        )

        return forum
