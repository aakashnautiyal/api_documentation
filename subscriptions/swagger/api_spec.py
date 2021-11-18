from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from subscriptions.swagger.schemas.sample_endpoint.request_schemas import SampleEndpointInput
from subscriptions.swagger.schemas.sample_endpoint.response_schemas import SampleEndpointOutput, SampleEndpointError

description_component = """
This component is used for taking user defined input parameters and based on it produce a randomized list of integers.
"""

settings = {"info": {"description": description_component}}

spec = APISpec(
    title="MSP : My sample project",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(),MarshmallowPlugin()],
    **settings
)

# register schemas with spec
spec.components.schema('SampleEndpointInput', schema=SampleEndpointInput)
spec.components.schema('SampleEndpointOutput', schema=SampleEndpointOutput)
spec.components.schema('SampleEndpointError', schema=SampleEndpointError)

description_collection = """Collection of all endpoints related to Subscriptions"""

# add swagger tags that are used for endpoint annotation
tags = [
    {
        "name": "Subscriptions",
        "description": description_collection
    }
]

for tag in tags:
    print(f"Adding tag : {tag['name']}")
    spec.tag(tag)
