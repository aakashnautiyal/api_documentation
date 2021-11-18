from subscriptions import subscriptions_api
from subscriptions.controllers import *

subscriptions_api.add_resource(
    SampleController, "/sample_endpoint", methods=["GET", "POST"], endpoint="sample_endpoint"
)
