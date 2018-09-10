from marshmallow import Schema, fields
from blogextractor.model import (
    UserSchema,
    PostSchema
)


class Topic(object):
    def __init__(
        self, _id, title=None, url=None, rank=None, number_of_posts=None, number_of_views=None,
        creator=None, last_comment_by=None, last_comment_at=None,
        number_of_pages=None, comments=None, retrieved_on=None
    ):
        self.id = _id
        self.title = title
        self.url = url
        self.rank = rank
        self.number_of_posts = number_of_posts
        self.number_of_views = number_of_views
        self.creator = creator
        self.last_comment_by = last_comment_by
        self.last_comment_at = last_comment_at
        self.number_of_pages = number_of_pages
        self.comments = comments
        self.retrieved_on = retrieved_on


class TopicSchema(Schema):

    class Meta:
        ordered = True

    id = fields.String()
    title = fields.String()
    url = fields.String()
    rank = fields.Integer()
    number_of_posts = fields.Integer()
    number_of_views = fields.Integer()
    creator = fields.Nested(UserSchema)
    last_comment_by = fields.Nested(UserSchema)
    last_comment_at = fields.DateTime()
    number_of_pages = fields.Integer()
    comments = fields.Nested(PostSchema, allow_none=True)
    retrieved_on = fields.DateTime()





