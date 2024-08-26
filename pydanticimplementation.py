from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str


user = User(id="0001", name="Hemanth", email="hsk@gmail.com")
print(user)
