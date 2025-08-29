from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, FilePath, DirectoryPath


class Settings(BaseSettings):
    """Application settings loaded from environment variables and .env file."""

    # Required settings without default values
    odoo_db_name: str
    odoo_config_path: FilePath  #  Pydantic's FilePath for automatic validation
    odoo_repo_path: DirectoryPath
    odoo_python_site_packages_path: DirectoryPath
    jwt_secret_key: SecretStr  # SecretStr for sensitive data

    ## Optional settings with default values
    jwt_expire_days: int = 7
    jwt_algorithm: str = "HS256"

    # Pydantic configuration for how to load settings
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False  # Environment variables are case-insensitive by default
    )


# Create a singleton instance to be used across the application
settings = Settings()
