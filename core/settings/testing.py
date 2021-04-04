from core.settings.base import Config


class TestingConfig(Config):
    """ Configuration class for site development environment """

    DEBUG = True
    DEVELOPMENT = True
    TESTING = True
    DATABASE = "mysql://task_manager:y5nhyen7s650u42h@db-mysql-ams3-96053-do-user-7909648-0.b.db.ondigitalocean.com:25060/task_manager"

