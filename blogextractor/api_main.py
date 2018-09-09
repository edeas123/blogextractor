from flask import Flask
from flask_restful import Api
from blogcrawler.resources import (
    PageResource,
    ForumResource,
    TopicResource,
    # BlogResource
)
from blogcrawler.config import load_config
# TODO: use the __init__ module import and find out why


def create_app(config) -> Flask:
    # create the app
    app = Flask(
        __name__
    )

    # TODO:
    # use the passed config object to
    # update the app config
    app.config.from_object(config)

    api = Api(app)

    # add the resources: should be imported first
    # TODO: add api to pull the forum info
    # TODO: add api to pull the page data for a specified page
    # TODO: add api to pull the data for a particular topic url

    # api.add_resource(
    #     BlogResource,
    #     '/{0}/'.format(config.API_PATH)
    # )
    # return a json object of Forum model in forum.py
    api.add_resource(
        ForumResource,
        '/{0}/forum/'.format(
            config.API_PATH
        )
    )
    api.add_resource(
        PageResource,
        '/{0}/page/'.format(
            config.API_PATH
        )
    )
    api.add_resource(
        TopicResource,
        '/{0}/topic/'.format(
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