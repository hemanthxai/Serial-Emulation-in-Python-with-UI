from pydantic import BaseModel
import yaml


class Config(BaseModel):
    emulators: list


def load_config(path: str) -> Config:
    with open(path, "r") as file:
        data = yaml.safe_load(file)
    return Config(**data)
