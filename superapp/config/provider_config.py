import hvac
from sitri.providers.contrib.system import SystemConfigProvider
from sitri.providers.contrib.vault import VaultKVConfigProvider
from sitri.settings.contrib.vault import VaultKVSettings

configurator = SystemConfigProvider(prefix="superapp")
ENV = configurator.get("env")

is_local_mode = ENV == "local"
local_mode_file_path = configurator.get("local_mode_file_path")


def vault_client_factory() -> hvac.Client:
    client = hvac.Client(url=configurator.get("vault_api"))

    client.auth_approle(
        role_id=configurator.get("role_id"),
        secret_id=configurator.get("secret_id"),
    )

    return client


provider = VaultKVConfigProvider(
    vault_connector=vault_client_factory,
    mount_point=f"{configurator.get('app_name')}/{ENV}",
)


class BaseConfig(VaultKVSettings.VaultKVSettingsConfig):
    provider = provider
    local_mode = is_local_mode
    local_provider_args = {"json_path": local_mode_file_path}
