from subscriptions.managers import *
from flask_restful import Resource
from flask import request
from subscriptions.settings import CONFIGURATIONS
from subscriptions.swagger.utils import docstring_parameter


class SampleController(Resource):
    @staticmethod
    @docstring_parameter(hosted_url=CONFIGURATIONS.get("hosted_url"))
    def get():
        """
            Endpoint to generate random list of size 10 between 1 and 10
            ---
             description: This API is used for generation of list of integers.
             summary: This endpoint is used for generation of list of integers.
             servers:
              - url : {hosted_url}
             responses:
               '200':
                 description: Successful Randomization
                 content:
                   application/json:
                     schema: SampleModelSchema
               '500':
                 description: Internal server error
                 content:
                   application/json:
                     schema: SampleEndpointError
             tags:
               - Subscriptions
        """
        return {"random_list": SampleManager.list(0, 100, 10)}

    @staticmethod
    @docstring_parameter(hosted_url=CONFIGURATIONS.get("hosted_url"))
    def post():
        """
            Endpoint to generate random list of user defined size and range
            ---
             description: This API is used for generation of list of integers.
             summary: This endpoint is used for generation of list of integers.
             servers:
              - url : {hosted_url}
             requestBody:
               content:
                 application/json:
                   schema: SampleEndpointInput
             responses:
               '200':
                 description: Successful Randomization
                 content:
                   application/json:
                     schema: SampleEndpointOutput
               '500':
                 description: Internal server error
                 content:
                   application/json:
                     schema: SampleEndpointError
             tags:
               - Subscriptions
        """
        input_json = request.json
        output_list = SampleManager.list(input_json["start"], input_json["end"], input_json["size"])
        return {"random_list": output_list}
