from marshmallow import Schema, fields


class CourseSchema(Schema):
    id = fields.Str()
    title = fields.Str()
    duration = fields.Float()
    created_at = fields.Str()
    updated_at = fields.Str()
