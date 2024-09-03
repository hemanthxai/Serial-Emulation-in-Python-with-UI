import yaml
from pydantic import BaseModel

class SerialConfig(BaseModel):
    port: str
    baudrate: int
    timeout: int
    delay: int

class SensorConfig(BaseModel):
    min_value: int
    max_value: int
    unit: str

class Config(BaseModel):
    serial: SerialConfig
    sensors: dict

    @classmethod
    def from_yaml(cls, path: str):
        with open(path, 'r') as file:
            data = yaml.safe_load(file)
            return cls(**data)
