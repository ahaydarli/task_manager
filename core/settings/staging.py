from core.settings.base import Config


class StagingConfig(Config):
    """ Configuration class for site production environment """

    DEBUG = False
    TESTING = False
    DATABASE = "mysql://root:@127.0.0.1:3306/task_manager"

