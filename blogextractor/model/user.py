from marshmallow import Schema, fields


class User(object):
    def __init__(
        self, name=None, gender=None, last_seen=None
    ):
        self.name = name
        self.gender = gender
        self.last_seen = last_seen


class UserSchema(Schema):
    name = fields.String()
    gender = fields.String()
    last_seen = fields.DateTime()
