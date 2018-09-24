from marshmallow import Schema, fields
from blogextractor.model import (
    TopicSchema,
    UserSchema
)
from uuid import uuid4


class Page(object):
    def __init__(
        self, forum, page_number=None, topics=None, viewers=None,
        number_of_guests=None, retrieved_on=None
    ):

        self.forum = forum
        self.page_number = page_number
        self.topics = topics
        self.viewers = viewers
        self.number_of_guests = number_of_guests
        self.retrieved_on = retrieved_on


class PageSchema(Schema):

    class Meta:
        ordered = True

    page_number = fields.Integer()
    forum = fields.Nested('ForumSchema', only='name')
    topics = fields.Nested(TopicSchema, many=True, only=('id', 'title'))
    viewers = fields.Nested(UserSchema, only='name')
    number_of_guests = fields.Integer()
    retrieved_on = fields.DateTime()
