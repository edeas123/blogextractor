from marshmallow import Schema, fields
from blogextractor.model import TopicSchema, UserSchema


class Forum(object):
    def __init__(
        self, name=None, url=None, sub_forums=None,
        page_number=None, number_of_pages=None,
        topics=None, viewers=None, number_of_guests=None,
        ad_rate=None, ad_period=None,
        percent_discount=None, retrieved_on=None
    ):

        self.name = name
        self.url = url
        self.sub_forums = sub_forums
        self.page_number = page_number
        self.topics = topics
        self.viewers = viewers,
        self.number_of_guests = number_of_guests
        self.ad_rate = ad_rate
        self.ad_period = ad_period
        self.percent_discount = percent_discount
        self.number_of_pages = number_of_pages
        self.retrieved_on = retrieved_on


class ForumSchema(Schema):

    class Meta:
        ordered = True

    name = fields.String()
    url = fields.String()
    ad_rate = fields.Float()
    ad_period = fields.String()
    percent_discount = fields.Float()
    sub_forums = fields.Nested('self', many=True, only='name')
    number_of_pages = fields.Integer()
    page_number = fields.Integer()
    topics = fields.Nested(TopicSchema, many=True)
    viewers = fields.Nested(UserSchema, many=True, only=['name'])  # fix
    number_of_guests = fields.Integer()
    retrieved_on = fields.DateTime()
