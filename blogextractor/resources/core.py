from flask_restful import Resource, reqparse
from marshmallow.exceptions import ValidationError
from requests import HTTPError
from datetime import datetime
from blogextractor._version import API_PATH


class BaseResource(Resource):

    _item = ""
    _endpoint = ""

    @classmethod
    def add_resource(cls, api):
        list_endpoint = f'{API_PATH}/{cls._endpoint}'
        single_endpoint = f'{list_endpoint}/{cls._item}'
        api.add_resource(cls, list_endpoint, single_endpoint)

    def get(self):

        # parse and retrieve request's arguments
        parser = reqparse.RequestParser()
        parser.add_argument('url', type=str)

        args = parser.parse_args()
        url = args['url']

        # use the blog name to get the correct extractor
        status = 200
        error = None
        result = None

        try:
            data = self.read(url=url)
            result = self.schema.dump(data, many=self.many)
        except TypeError as e:
            status = 422
            error = str(e)
        except HTTPError as e:
            status = 404
            error = str(e)
        except ValidationError as e:
            status = 422
            error = str(e)
        except Exception as e:
            status = 500
            error = str(e)

        # return data and status code
        return {
            'data': result,
            'status_code': status,
            'request_time': '',
            'error': error,
            'timestamp': str(datetime.utcnow())
        }, status
