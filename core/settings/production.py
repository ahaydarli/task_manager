from core.settings.base import Config


class ProductionConfig(Config):
    """ Configuration class for site production environment """

    DEBUG = False
    TESTING = False
    DATABASE = "mysql://task_manager:y5nhyen7s650u42h@db-mysql-ams3-96053-do-user-7909648-0.b.db.ondigitalocean.com:25060/task_manager"
