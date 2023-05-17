from pydantic import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_database_url: str = "postgresql+psycopg2://postgres:567234@localhost:5432/postgres"
    jwt_secret_key: str = "secret"
    jwt_algorithm: str = "HS256"
    mail_username: str = "example@meta.ua"
    mail_password: str = "password"
    mail_from: str = "example@meta.ua"
    mail_port: int = 465
    mail_server: str = "smtp.test.com"
    redis_host: str = 'localhost'
    redis_port: int = 6379
    cloudinary_name = "cloudinary name"
    cloudinary_api_key = "000000000000000000"
    cloudinary_api_secret = "secret"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
