from marshmallow import Schema, fields
from blogcrawler.model import UserSchema


class Post(object):
    def __init__(
        self, _id, user=None, ts=None, number_of_likes=None,
        number_of_shares=None, requotes=None, number_of_links=None,
        number_of_images=None
    ):
        self.id = _id
        self.user = user
        self.ts = ts
        self.number_of_likes = number_of_likes
        self.number_of_shares = number_of_shares
        self.number_of_links = number_of_links
        self.number_of_images = number_of_images
        self.requotes = requotes


class PostSchema(Schema):

    class Meta:
        ordered = True

    id = fields.Integer()
    user = fields.Nested(UserSchema, only='name')
    ts = fields.DateTime()
    number_of_likes = fields.Integer()
    number_of_shares = fields.Integer()
    requotes = fields.Boolean()
    number_of_links = fields.Integer()
    number_of_images = fields.Integer()
