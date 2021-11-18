from flask import Flask, jsonify
from flask_restful import Api
from subscriptions.swagger.swagger import swagger_ui_blueprint
from subscriptions.settings import CONFIGURATIONS
from subscriptions.swagger.api_spec import spec

app = Flask(__name__)
app.register_blueprint(swagger_ui_blueprint, url_prefix=CONFIGURATIONS.get("SWAGGER_URL"))
subscriptions_api = Api(app)

__import__("subscriptions.routes")

with app.app_context():
    for func_name in app.view_functions:
        if func_name == "static":
            continue
        view_func = app.view_functions[func_name]
        print("@@@@@@@", view_func)
        spec.path(view=view_func)


@app.route("/api/swagger.json")
def create_swagger_spec():
    """Swagger API definition"""
    return jsonify(spec.to_dict())
