import os
import sys
import random
import threading
import serial
if os.getenv("WSL_DISTRO_NAME"):  # Check if running under WSL
    os.environ["XDG_SESSION_TYPE"] = "x11"
elif os.getenv("XDG_SESSION_TYPE") == "wayland":
    os.environ["XDG_SESSION_TYPE"] = "x11"

import glfw
import OpenGL.GL as gl
import imgui
from imgui.integrations.glfw import GlfwRenderer




active_sensors = {
    "Temperature": False,
    "Pressure": False,
    "Water Level": False,
}

sensor_values = {
    "Temperature": "0°C",
    "Pressure": "0 hPa",
    "Water Level": "0 meters",
}

output_text = "Output Window"
path_to_font = None 

secondary_window_text = []




def update_sensor_value(sensor_name: str):
    sensor_data = get_sensordata(sensor_name)
    if sensor_name == "Temperature":
        sensor_values[sensor_name] = sensor_data[0]
    elif sensor_name == "Pressure":
        sensor_values[sensor_name] = sensor_data[1]
    elif sensor_name == "Water Level":
        sensor_values[sensor_name] = sensor_data[2]

def get_sensordata(sensor: str):

    ser1 = serial.Serial('/dev/pts/6', 9600, timeout=1)
    ser2 = serial.Serial('/dev/pts/8', 9600, timeout=1)
    ser3 = serial.Serial('/dev/pts/10', 9600, timeout=1)

    data1 = ""
    data2 = ""
    data3 = ""

    while True:
        if sensor == "Temperature":
            data1 = ser1.readline().decode('utf-8').strip()
            if data1:
                print(f"Received temperature value: {data1}°C")
                return [data1, data2, data3]
        elif sensor == "Pressure":
            data2 = ser2.readline().decode('utf-8').strip()
            if data2:
                print(f"Received pressure value: {data2}°C")
                return [data1, data2, data3]
        elif sensor == "Water Level":
            data3 = ser3.readline().decode('utf-8').strip()
            if data3:
                print(f"Received water level value: {data3}°C")
                return [data1, data2, data3]


def generate_all_thread():
    update_sensor_value("Temperature")
    update_sensor_value("Pressure")
    update_sensor_value("Water Level")

def frame_commands():
    global output_text, secondary_window_text
    gl.glClearColor(0.1, 0.1, 0.1, 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    io = imgui.get_io()

    if io.key_ctrl and io.keys_down[glfw.KEY_Q]:
        sys.exit(0)

    if imgui.begin_main_menu_bar():
        if imgui.begin_menu("EXIT", True):
            sys.exit(0)
            imgui.end_menu()
        imgui.end_main_menu_bar()

    imgui.begin("Sensor Data")
    for label in active_sensors.copy().keys():
        if imgui.button(f"Show {label} Value"):
            active_sensors[label] = True
            output_text = f"{label} updated to {sensor_values[label]}"
        imgui.same_line()
        if imgui.button(f"Update {label}"):
            update_sensor_value(label)
            output_text = f"{label} updated to {sensor_values[label]}"
        imgui.same_line()
        if imgui.button(f"Add {label} to Secondary"):
            secondary_window_text.append(f"{label}: {sensor_values[label]}")
    
    if imgui.button("Generate All"):
        # Start a new thread to update all sensor values
        threading.Thread(target=generate_all_thread, daemon=True).start()
    
    imgui.end()

    # Sensor Value Windows
    for label, enabled in active_sensors.copy().items():
        if enabled:
            imgui.begin(f"{label} Sensor")
            imgui.text(f"{label}: {sensor_values[label]}")
            imgui.end()

    # Secondary Window
    imgui.begin("Secondary Window")
    if imgui.button("Clear"):
        secondary_window_text.clear()
    imgui.text("Secondary Window Content:")
    for text in secondary_window_text:
        imgui.text(text)
    imgui.end()

    # Output Window
    imgui.begin("Output Window")
    imgui.text(output_text)
    imgui.end()

def render_frame(impl, window, font): # type: ignore
    glfw.poll_events()
    impl.process_inputs()
    imgui.new_frame()

    gl.glClearColor(0.1, 0.1, 0.1, 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    if font is not None:
        imgui.push_font(font)
    frame_commands()
    if font is not None:
        imgui.pop_font()

    imgui.render()
    impl.render(imgui.get_draw_data())
    glfw.swap_buffers(window)

def impl_glfw_init():
    width, height = 1000, 800
    window_name = "Emulate Serial Devices"

    if not glfw.init():
        print("Could not initialize OpenGL context")
        sys.exit(1)

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    window = glfw.create_window(int(width), int(height), window_name, None, None)
    glfw.make_context_current(window)

    if not window:
        glfw.terminate()
        print("Could not initialize Window")
        sys.exit(1)

    return window

def main():
    imgui.create_context()
    window = impl_glfw_init()

    impl = GlfwRenderer(window)

    io = imgui.get_io()
    font = io.fonts.add_font_from_file_ttf(None, 30) if path_to_font is not None else None
    impl.refresh_font_texture()

    while not glfw.window_should_close(window):
        render_frame(impl, window, font)

    impl.shutdown()
    glfw.terminate()

if __name__ == "__main__":
    main()
