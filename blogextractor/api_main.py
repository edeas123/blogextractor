from flask import Flask
from flask_restful import Api
from blogextractor.resources import (
    ForumResource,
    CommentResource,
)
from blogextractor.config import load_config
from blogextractor._version import API_PATH


def create_app(config) -> Flask:

    # create the app
    app = Flask(
        __name__
    )

    # use the passed config object to update the app config
    app.config.from_object(config)

    api = Api(app)

    api.add_resource(
        ForumResource,
        '{0}/forum/'.format(
            API_PATH
        )
    )
    api.add_resource(
        CommentResource,
        '{0}/comment/'.format(
            API_PATH
        )
    )

    return app


def uwsgi(environ, start_response):
    app = create_app(load_config())

    return app.wsgi_app(environ, start_response)
