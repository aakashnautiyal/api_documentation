from marshmallow import Schema, fields, validate


class SampleEndpointInput(Schema):
    """
    Request body schema
    """
    not_blank = validate.Length(min=1, error="Field can't be blank")
    start = fields.Integer(example=1, description="Starting integer for random list", validate=not_blank,
                           required=True)
    end = fields.Integer(example=10, description="ending integer for random list", validate=not_blank, required=True)
    size = fields.Integer(example=5, description="Length for random list", validate=not_blank,
                          required=True)
