from marshmallow import Schema, fields

class User(object):
    def __init__(
        self, name, gender=None
    ):
        self.name = name
        self.gender = gender


class UserSchema(Schema):
    name = fields.String()
    gender = fields.String()  # TODO: how do you handle just two (like enum): M & F
    comments = fields.Nested('PostSchema', many=True)
    # TODO: can we also add reference to the posted articles,
    # it will be interesting because it is already ref from there
