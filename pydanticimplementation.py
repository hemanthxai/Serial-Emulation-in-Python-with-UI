from pydantic import (
    BaseModel,
    EmailStr,
    AnyUrl,
    PositiveInt,
    validator,
)


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


# Using inbuilt Validators in Pydantic


class UserProfile(BaseModel):

    username: str

    age: PositiveInt

    salary: PositiveInt

    email: EmailStr

    gitwebsite: AnyUrl

    bio: str

    profile_picture: AnyUrl


newuser = UserProfile(
    username="Hemanth",
    age=21,
    salary=1000,
    debt=0.0,
    email="user@example.com",
    gitwebsite="https://e.com",
    bio="IoT Python developer",
    profile_picture="https://github.com/hemanthxai/TechnoCulture-Research/",
)
print(newuser)
