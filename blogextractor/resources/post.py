from flask_restful import Resource, reqparse
from blogextractor.extractors.core import (
    get_extractor
)
from blogextractor.model import PostSchema


class PostResource(Resource):

    schema = PostSchema()

    def get(self):

        # parse and retrieve request's arguments
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('blog', type=str)
        parser.add_argument('page_number', type=int)

        args = parser.parse_args()

        blog = args['blog']
        topic_id = args['id']
        page_number = args['page_number'] or 0

        # use the blog name to get the correct extractor
        result = {}
        try:
            post_extractor = get_extractor(blog, 'post')
            result = post_extractor(
                blog=blog,
                topic_id=topic_id,
                page_number=page_number
            ).extract()

        except Exception:
            # TODO: return appropriate error message
            pass

        # return data and status code
        # TODO: first check for errors in dump
        return self.schema.dump(result, many=True), 200
