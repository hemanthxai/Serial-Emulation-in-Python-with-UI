from pydantic import BaseModel, EmailStr, AnyUrl, PositiveInt, validator
from dataclasses import dataclass
from typing import Optional, Tuple
import imgui
from imgui.integrations.glfw import GlfwRenderer
import glfw
import random
import time
import argparse
from enum import Enum


# Custom exceptions
class TemperatureError(Exception):
    pass


# Custom validator function
def validate_temperature(temp: float) -> float:
    if temp > 100 or temp < -100:
        raise TemperatureError(f"Temperature {temp} must be between -100°C and 100°C")
    return temp


# User Model
class User(BaseModel):
    id: int
    name: str
    email: EmailStr

    @validator("id")
    def validate_id(cls, value: int) -> int:
        if value < 0:
            raise ValueError("ID value must be greater than 0")
        return value


# User Profile Model
class UserProfile(BaseModel):
    username: str
    age: PositiveInt
    salary: PositiveInt
    email: EmailStr
    gitwebsite: AnyUrl
    bio: str
    profile_picture: Optional[AnyUrl] = None

    @validator("bio")
    def validate_bio(cls, value: str) -> str:
        if len(value) < 10:
            raise ValueError("Bio must be at least 10 characters long")
        return value


# Dataclass for Sensor Data
@dataclass
class SensorsAvailable:
    temp1: float
    temp2: float
    temp3: float


# Generate random temperature data
def generate_random_temperatures() -> SensorsAvailable:
    return SensorsAvailable(
        temp1=random.uniform(-100, 120),
        temp2=random.uniform(-50, 100),
        temp3=random.uniform(-100, 120),
    )


# GUI for displaying sensor data
def gui(update_interval: float = 2.0) -> None:
    if not glfw.init():
        print("Failed to initialize GLFW")
        return

    window = glfw.create_window(700, 800, "Temperature Sensor Data", None, None)
    if not window:
        print("Failed to create GLFW window")
        glfw.terminate()
        return

    glfw.make_context_current(window)
    imgui.create_context()
    impl = GlfwRenderer(window)

    last_update_time = time.time()
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


# CLI using argparse
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Temperature Sensor Data Display")
    parser.add_argument(
        "--interval", type=float, default=1.5, help="Update interval for sensor data"
    )
    return parser.parse_args()


# Enum for Status
class Status(Enum):
    PENDING = "ZERO"
    IN_PROGRESS = "ONE"


# Main function
def main() -> None:
    args = parse_args()

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

    print("User: ")
    print(user)
    print("\nUserProfile: ")
    print(newuser)

    # JSON serialization
    user_json = newuser.json()
    print("\nSerialized JSON:")
    print(user_json)

    # Enum usage
    status_pending = Status.PENDING
    status_in_progress = Status.IN_PROGRESS
    print("Tasks:")
    print("Tasks pending: ", status_pending.value)
    print("Tasks in progress: ", status_in_progress.value)

    # Run GUI with update interval from CLI
    gui(update_interval=args.interval)


if __name__ == "__main__":
    main()
