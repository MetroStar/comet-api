from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    API_PREFIX: str = ""
    DATABASE_URL: str = "sqlite:///./db.sqlite3"
    OIDC_CONFIG_URL: str | None = None


settings = Settings()
