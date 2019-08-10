import os


class Config(object):

    # flask settings
    PORT = os.environ.get('PORT', 5000)
    DEBUG = os.environ.get('DEBUG', True)
    TESTING = os.environ.get('TESTING', True)
    ENV = os.environ.get('ENV', "development")


class ProductionConfig(Config):

    # flask settings
    PORT = os.environ.get('PORT', 5000)
    DEBUG = os.environ.get('DEBUG', False)
    TESTING = os.environ.get('TESTING', False)
    ENV = os.environ.get('ENV', "production")


def load_config() -> Config:
    if os.environ.get('APP_ENV') in ["docker", "kubernetes"]:
        return ProductionConfig()

    return Config()
