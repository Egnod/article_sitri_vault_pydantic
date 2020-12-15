from pydantic import Field
from sitri.settings.contrib.vault import VaultKVSettings

from superapp.config.provider_config import BaseConfig, provider


class DBSettings(VaultKVSettings):
    user: str = Field(..., vault_secret_key="username")
    password: str = Field(...)
    host: str = Field(...)
    port: int = Field(...)

    class Config(BaseConfig):
        provider = provider
        default_secret_path = "db"
        local_mode_path_prefix = "db"
