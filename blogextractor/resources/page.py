from flask_restful import Resource, reqparse
from blogextractor.extractors.core import (
    get_extractor
)
from blogextractor.model import PageSchema


class PageResource(Resource):

    schema = PageSchema()

    def get(self):

        # parse and retrieve request's arguments
        parser = reqparse.RequestParser()
        parser.add_argument('blog', type=str)
        parser.add_argument('forum', type=str)
        parser.add_argument('page_number', type=int)

        args = parser.parse_args()

        blog = args['blog']
        forum = args['forum']
        page_number = args['page_number'] or 0

        # use the blog name to get the correct extractor
        result = {}
        try:
            page_extractor = get_extractor(blog, 'page')
            result = page_extractor(
                blog=blog,
                forum=forum,
                page_number=page_number
            ).extract()

        except Exception:
            # TODO: return appropriate error message
            pass

        # return data and status code
        # TODO: first check for errors in dump
        return self.schema.dump(result), 200
