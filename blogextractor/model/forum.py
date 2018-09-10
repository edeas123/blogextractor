from marshmallow import Schema, fields
from blogextractor.model import PageSchema


class Forum(object):
    def __init__(
        self, name=None, sub_forums=None,
        number_of_pages=None, forum_pages=None,
        ad_rate=None, ad_period=None,
        percent_discount=None
    ):

        self.name = name
        self.sub_forums = sub_forums
        self.ad_rate = ad_rate
        self.ad_period = ad_period
        self.percent_discount = percent_discount
        self.number_of_pages = number_of_pages
        self.forum_pages = forum_pages


class ForumSchema(Schema):

    class Meta:
        ordered = True

    name = fields.String()
    ad_rate = fields.Float()
    ad_period = fields.String()
    percent_discount = fields.Float()
    sub_forums = fields.Nested('self', many=True, only='name')
    number_of_pages = fields.Integer()
    forum_pages = fields.Nested(PageSchema, many=True)