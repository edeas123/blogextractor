from flask_restful import Resource, reqparse
from blogextractor.extractors.util import (
    get_extractor
)
from blogextractor.model import ForumSchema
from blogextractor.util import get_domain
from marshmallow.exceptions import ValidationError
from requests import HTTPError


class ForumResource(Resource):

    schema = ForumSchema()

    def get(self):

        # parse and retrieve request's arguments
        parser = reqparse.RequestParser()
        parser.add_argument('url', type=str)

        args = parser.parse_args()
        url = args['url']

        # use the blog name to get the correct extractor
        try:
            domain = get_domain(url)
            extractor = get_extractor(domain, 'forum')
            data = extractor(url=url).extract()
        except TypeError as e:
            # log the error to sumo logic
            return str(e), 422
        except HTTPError as e:
            # log the error to sumo logic
            return str(e), 404
        except Exception as e:
            # log unknown exception
            return e.with_traceback()

        # return data and status code
        try:
            result = self.schema.dump(data)
        except ValidationError as e:
            return str(e), 422

        return result, 200
