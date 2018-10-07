from marshmallow import Schema, fields
from blogextractor.model import UserSchema


class Comment(object):
    def __init__(
        self, _id, title=None, created_by=None, created_on=None,
        number_of_likes=None, number_of_shares=None, requotes=None,
        number_of_links=None, number_of_images=None,
        number_of_words=None, retrieved_on=None
    ):
        self.id = _id
        self.title = title
        self.created_by = created_by
        self.created_on = created_on
        self.number_of_likes = number_of_likes
        self.number_of_shares = number_of_shares
        self.number_of_links = number_of_links
        self.number_of_images = number_of_images
        self.requotes = requotes
        self.number_of_words = number_of_words
        self.retrieved_on = retrieved_on


class CommentSchema(Schema):

    class Meta:
        ordered = True

    id = fields.Integer()
    title = fields.Nested('TopicSchema', only='id')
    created_by = fields.Nested(UserSchema, only='name')
    created_on = fields.DateTime()
    number_of_likes = fields.Integer()
    number_of_shares = fields.Integer()
    requotes = fields.Boolean()
    number_of_links = fields.Integer()
    number_of_images = fields.Integer()
    number_of_words = fields.Integer()
    retrieved_on = fields.DateTime()
