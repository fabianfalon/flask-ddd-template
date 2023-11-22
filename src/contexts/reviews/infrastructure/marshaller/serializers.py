from marshmallow import Schema, fields


class ReviewSchema(Schema):
    review_id = fields.Str()
    course_id = fields.Str()
    comment = fields.Str()
    created_at = fields.Str()
    updated_at = fields.Str()
