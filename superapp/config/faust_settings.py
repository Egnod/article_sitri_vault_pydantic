from typing import Dict

from pydantic import BaseModel, Field
from sitri.settings.contrib.vault import VaultKVSettings

from superapp.config.provider_config import provider


class AgentConfig(BaseModel):
    partitions: int = Field(...)
    concurrency: int = Field(...)


class FaustSettings(VaultKVSettings):
    app_name: str = Field(...)
    default_partitions_count: int = Field(..., vault_secret_key="partitions_count")
    default_concurrency: int = Field(..., vault_secret_key="agent_concurrency")
    agents: Dict[str, AgentConfig] = Field(
        default=None, vault_secret_key="agents_specification"
    )

    class Config:
        provider = provider
        default_secret_path = "faust"
