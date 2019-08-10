from blogextractor.api_main import create_app
from blogextractor.config import load_config


if __name__ == "__main__":

    config = load_config()
    app = create_app(config)
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG)
