from pydantic import BaseModel, Field, ValidationError
import yaml

class SensorConfig(BaseModel):
    type: str
    min_value: int
    max_value: int
    unit: str

class SensorsConfig(BaseModel):
    temperature: SensorConfig
    pressure: SensorConfig
    water_level: SensorConfig

class SerialConfig(BaseModel):
    port: str
    baudrate: int
    timeout: float
    delay: int

class LoggingConfig(BaseModel):
    level: str
    format: str

class AppConfig(BaseModel):
    name: str
    version: str

class Config(BaseModel):
    serial: SerialConfig
    sensors: SensorsConfig
    logging: LoggingConfig
    app: AppConfig

def load_config(config_file: str) -> dict:
    """Load a YAML file and return it as a dictionary."""
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)

def get_config() -> Config:
    """Load and return the merged configuration."""
    try:
        # Load each YAML config file
        serial_config = load_config('serial_config.yaml')
        sensor_config = load_config('sensor_config.yaml')
        app_config = load_config('app_config.yaml')

        # Merge configurations into one
        config_data = {
            **serial_config,
            **sensor_config,
            **app_config
        }

        # Validate and return the configuration
        return Config(**config_data)
    except ValidationError as e:
        print(f"Configuration Error: {e}")
        exit(1)
