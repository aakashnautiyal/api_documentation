from flask_swagger_ui import get_swaggerui_blueprint
from subscriptions.settings import CONFIGURATIONS

swagger_ui_blueprint = get_swaggerui_blueprint(
    CONFIGURATIONS.get("SWAGGER_URL"),
    CONFIGURATIONS.get("API_URL"),
    config={
        "app_name": "Subscriptions"
    }
)
