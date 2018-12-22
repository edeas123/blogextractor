from blogextractor.resources.core import BaseResource
from blogextractor.model import CommentSchema
from blogextractor.extractors.util import (
    get_extractor
)
from blogextractor.util import get_domain


class CommentResource(BaseResource):

    schema = CommentSchema()
    many = True

    def read(self, url):

        domain = get_domain(url)
        extractor = get_extractor(domain, 'comment')
        data = extractor(url=url).extract()

        return data
