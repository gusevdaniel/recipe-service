from starlette.config import Config

config = Config(".env")

DB_USER = config("DB_USER", cast=str, default="")

DB_USERNAME = config("DB_USERNAME", cast=str, default="")
DB_PASSWORD = config("DB_PASSWORD", cast=str, default="")
DB_NAME = config("DB_NAME", cast=str, default="")
DB_HOST = config("DB_HOST", cast=str, default="")
DB_PORT = config("DB_PORT", cast=str, default="")

DATABASE_URL = (
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)

ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"

SECRET_KEY = config("SECRET_KEY", cast=str, default="")
ADMIN_KEY = config("ADMIN_KEY", cast=str, default="")
