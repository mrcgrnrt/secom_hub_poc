from environs import Env

env = Env()
env.read_env()

DEBUG = env.bool("FLASK_DEBUG", default=False)
SECRET_KEY = env.str("FLASK_SECRET_KEY")

DB_URL = env.str("DB_SERVER_URL", default="mongodb://localhost:27017")
DB_DATABASE_NAME = env.str("DB_DATABASE_NAME", default="secom-registry")
DB_COLLECTION_NAME = env.str("DB_COLLECTION_NAME", default="nodes")

LOG_LEVEL = env.str("LOG_LEVEL", default="WARNING")

HOST = env.str("FLASK_HOST", default="127.0.0.1")
PORT = env.int("FLASK_PORT", default=5000)

