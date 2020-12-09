from pydantic import BaseModel, Field

from superapp.config.database_settings import DBSettings
from superapp.config.faust_settings import FaustSettings
from superapp.config.kafka_settings import KafkaSettings


class AppSettings(BaseModel):
    db: DBSettings = Field(default_factory=DBSettings)
    faust: FaustSettings = Field(default_factory=FaustSettings)
    kafka: KafkaSettings = Field(default_factory=KafkaSettings)
