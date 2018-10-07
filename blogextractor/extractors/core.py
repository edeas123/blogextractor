import requests


class Extractor(object):

    # request the html page from the page url
    @staticmethod
    def request_page(url: str) -> str:
        r = requests.get(url=url)
        r.raise_for_status()

        return r.text
