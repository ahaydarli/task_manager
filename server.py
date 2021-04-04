import os

from werkzeug.serving import run_simple

from core.factories import create_app, SettingsError


if os.environ["APP_SETTINGS"]:
    settings_name = os.environ["APP_SETTINGS"]
else:
    raise SettingsError("'APP_SETTINGS' environment " "variable is not defined")
flask_app = create_app(settings_name)


if __name__ == "__main__":
    run_simple(
        "0.0.0.0", 8080, flask_app, use_reloader=False, use_debugger=flask_app.config["DEBUG"]
    )
