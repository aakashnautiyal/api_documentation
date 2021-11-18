from marshmallow import Schema, fields


class SampleEndpointOutput(Schema):
    """
    Response body schema
    """
    random_list = fields.List(fields.Integer, example=[6, 2, 1, 5, 3], description="Randomized list of integers",
                              required=True)


class SampleEndpointError(Schema):
    """
    Error body schema
    """
    id = fields.String(required=True, metadata={
        'description': "request ID of particular request",
        'example': "a03dddd5c654434566bdac2ddee09e1c"
    })
    code = fields.Int(example=500, description="API specific code")
    message = fields.String(example="An exception was raised", description="API specific error")
    status = fields.Boolean(example=False)
