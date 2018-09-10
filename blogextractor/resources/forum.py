from flask_restful import Resource, reqparse
from blogextractor.extractors.core import (
    get_extractor
)
from blogextractor.model import ForumSchema


class ForumResource(Resource):

    schema = ForumSchema()

    def get(self):

        # parse and retrieve request's arguments
        parser = reqparse.RequestParser()
        parser.add_argument('blog', type=str)
        parser.add_argument('forum', type=str)

        args = parser.parse_args()

        blog = args['blog']
        forum = args['forum']

        # use the blog name to get the correct extractor
        result = {}
        try:
            page_extractor = get_extractor(blog, 'forum')
            result = page_extractor(
                blog=blog,
                forum=forum
            ).extract()

        except Exception:
            # TODO: return appropriate error message
            pass

        # return data and status code
        # TODO: first check for errors in dump
        return self.schema.dump(result), 200
