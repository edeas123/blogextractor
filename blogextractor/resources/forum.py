from blogextractor.extractors.util import (
    get_extractor
)
from blogextractor.resources.core import BaseResource
from blogextractor.model import ForumSchema
from blogextractor.util import get_domain


class ForumResource(BaseResource):

    schema = ForumSchema()
    many = False

    def read(self, url):

        domain = get_domain(url)
        extractor = get_extractor(domain, 'forum')
        data = extractor(url=url).extract()

        return data
