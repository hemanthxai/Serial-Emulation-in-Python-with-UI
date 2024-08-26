from pydantic import (
    BaseModel,
    EmailStr,
    AnyUrl,
    PositiveInt,
    validator,
)

# Custom Validator


class User(BaseModel):
    id: int
    name: str
    email: EmailStr

    @validator("id")
    def validate_id(cls, value):
        if value < 0:
            raise ValueError("ID value must be greater than 0")
        return value


# Create an instance of User
user = User(id=1, name="Hemanth", email="hsk@gmail.com")
print("User:")
print(user)

# Using built-in Validators in Pydantic


class UserProfile(BaseModel):
    username: str
    age: PositiveInt
    salary: PositiveInt
    email: EmailStr
    gitwebsite: AnyUrl
    bio: str
    profile_picture: AnyUrl = None  # Optional field with default value of None

    # Custom validator for 'bio' to ensure it is at least 10 characters long
    @validator("bio")
    def validate_bio(cls, value):
        if len(value) < 10:
            raise ValueError("Bio must be at least 10 characters long")
        return value


# Create an instance of UserProfile
newuser = UserProfile(
    username="Hemanth",
    age=21,
    salary=1000,
    email="user@example.com",
    gitwebsite="https://e.com",
    bio="IoT Python developer specializing in data validation",
    profile_picture="https://github.com/hemanthxai/TechnoCulture-Research/",
)
print("\nUserProfile:")
print(newuser)

# JSON Serialization
user_json = newuser.json()
print("\nSerialized JSON:")
print(user_json)
