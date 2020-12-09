from typing import Any, Dict

from pydantic import Field
from sitri.settings.contrib.vault import VaultKVSettings

from superapp.config.provider_config import configurator, provider


class KafkaSettings(VaultKVSettings):
    mechanism: str = Field(..., vault_secret_key="auth_mechanism")
    brokers: str = Field(...)
    auth_data: Dict[str, Any] = Field(...)

    class Config:
        provider = provider
        default_secret_path = "kafka"
        default_mount_point = f"{configurator.get('app_name')}/common"
