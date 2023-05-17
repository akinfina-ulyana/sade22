from marshmallow import Schema, fields, ValidationError


class MessageSchema(Schema):
    chat_id = fields.Int()
    message = fields.Str(required=True)

