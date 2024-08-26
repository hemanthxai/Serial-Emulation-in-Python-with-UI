from pydantic import BaseModel, EmailStr, validator


class User(BaseModel):
    id: int
    name: str
    email: EmailStr

    @validator("id")
    def validate_id(cls, value):
        if value < 0:
            raise ValueError("ID value must be greater than 0")
        return value


user = User(id=1, name="Hemanth", email="hsk@gmail.com")
print(user)
