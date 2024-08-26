from pydantic import BaseModel, EmailStr, AnyUrl, PositiveInt, validator
from dataclasses import dataclass
import imgui
from imgui.integrations.glfw import GlfwRenderer
import glfw
import random
import time


# custom exceptions
class TemperatureError(Exception):
    pass


# Custom validator function
def validate_temperature(temp):
    if temp > 100 or temp < -100:
        raise TemperatureError(f"Temperature {temp} must be between -100°C and 100°C")
    return temp


class User(BaseModel):
    id: int
    name: str
    email: EmailStr

    @validator("id")
    def validate_id(cls, value):
        if value < 0:
            raise ValueError("ID value must be greater than 0")
        return value


class UserProfile(BaseModel):
    username: str
    age: PositiveInt
    salary: PositiveInt
    email: EmailStr
    gitwebsite: AnyUrl
    bio: str
    profile_picture: AnyUrl = None  #

    @validator("bio")
    def validate_bio(cls, value):
        if len(value) < 10:
            raise ValueError("Bio must be at least 10 characters long")
        return value


user = User(id=1, name="Hemanth", email="hsk@gmail.com")
newuser = UserProfile(
    username="Hemanth",
    age=21,
    salary=1000,
    email="user@example.com",
    gitwebsite="https://e.com",
    bio="IoT Python developer",
    profile_picture="https://github.com/hemanthxai/TechnoCulture-Research/",
)


# dataclass for Sensor Data
@dataclass
class SensorsAvailable:
    temp1: float
    temp2: float
    temp3: float


# generate random temperature
def generate_random_temperatures():
    return SensorsAvailable(
        temp1=random.uniform(-100, 120),
        temp2=random.uniform(-50, 100),
        temp3=random.uniform(-100, 120),
    )


# GUI
def gui():
    if not glfw.init():
        print("Failed to initialize GLFW")
        return

    window = glfw.create_window(940, 900, "Temperature Sensor Data", None, None)
    if not window:
        print("Failed to create GLFW window")
        glfw.terminate()
        return

    glfw.make_context_current(window)
    imgui.create_context()
    impl = GlfwRenderer(window)

    last_update_time = time.time()
    update_interval = 2.0
    sensor_data = generate_random_temperatures()

    while not glfw.window_should_close(window):
        glfw.poll_events()
        impl.process_inputs()
        imgui.new_frame()

        imgui.begin("Temperature Sensor Data")
        imgui.text("Temperatures Recorded:")
        imgui.separator()

        current_time = time.time()

        if current_time - last_update_time >= update_interval:
            last_update_time = current_time
            sensor_data = generate_random_temperatures()

            try:
                temp1 = validate_temperature(sensor_data.temp1)
                temp2 = validate_temperature(sensor_data.temp2)
                temp3 = validate_temperature(sensor_data.temp3)

                imgui.text(f"Temperature 1: {temp1:.2f} °C")
                imgui.text(f"Temperature 2: {temp2:.2f} °C")
                imgui.text(f"Temperature 3: {temp3:.2f} °C")
            except TemperatureError as e:
                imgui.text(f"Error: {e}")

        imgui.end()
        imgui.render()
        impl.render(imgui.get_draw_data())
        glfw.swap_buffers(window)
        time.sleep(2)

    impl.shutdown()
    glfw.terminate()


if __name__ == "__main__":

    print("User: ")
    print(user)
    print("\nUserProfile: ")
    print(newuser)

    # JSON serialization
    user_json = newuser.json()
    print("\nSerialized JSON:")
    print(user_json)

    from enum import Enum

    class Status(Enum):
        PENDING = "ZERO"
        IN_PROGRESS = "ONE"

    status_pending = Status.PENDING
    status_in_progress = Status.IN_PROGRESS
    print("Tasks:")
    print("Tasks pending: ", status_pending.value)
    print("Tasks in progress: ", status_in_progress.value)

    # run GUI
    gui()
