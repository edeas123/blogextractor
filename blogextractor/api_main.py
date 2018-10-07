from flask import Flask
from flask_restful import Api
from blogextractor.resources import (
    ForumResource,
    CommentResource,
)
from blogextractor.config import load_config


def create_app(config) -> Flask:
    # create the app
    app = Flask(
        __name__
    )

    # use the passed config object to update the app config
    app.config.from_object(config)

    api = Api(app)

    # return a json object of Forum model in forum.py
    api.add_resource(
        ForumResource,
        '/{0}/forum/'.format(
            config.API_PATH
        )
    )
    api.add_resource(
        CommentResource,
        '/{0}/comment/'.format(
            config.API_PATH
        )
    )

    return app


if __name__ == "__main__":

    # read config from environment variables
    # or from file including things
    # like the port and debug mode
    config = load_config()
    app = create_app(config)
    app.run()
