from marshmallow import Schema, fields
from blogextractor.model import UserSchema


class Post(object):
    def __init__(
        self, _id, title=None, user=None, ts=None, number_of_likes=None,
        number_of_shares=None, requotes=None, number_of_links=None,
        number_of_images=None, retrieved_on=None
    ):
        self.id = _id
        self.title = title
        self.user = user
        self.ts = ts
        self.number_of_likes = number_of_likes
        self.number_of_shares = number_of_shares
        self.number_of_links = number_of_links
        self.number_of_images = number_of_images
        self.requotes = requotes
        self.retrieved_on = retrieved_on


class PostSchema(Schema):

    class Meta:
        ordered = True

    id = fields.Integer()
    title = fields.Nested('TopicSchema', only='title')
    user = fields.Nested(UserSchema, only='name')
    ts = fields.DateTime()
    number_of_likes = fields.Integer()
    number_of_shares = fields.Integer()
    requotes = fields.Boolean()
    number_of_links = fields.Integer()
    number_of_images = fields.Integer()
    retrieved_on = fields.DateTime()
