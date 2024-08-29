# # -*- coding: utf-8 -*-
import os
import sys
import random


if os.getenv("WSL_DISTRO_NAME"):  # Check if running under WSL
    os.environ["XDG_SESSION_TYPE"] = "x11"
elif os.getenv("XDG_SESSION_TYPE") == "wayland":
    os.environ["XDG_SESSION_TYPE"] = "x11"

import glfw
import OpenGL.GL as gl
import imgui
from imgui.integrations.glfw import GlfwRenderer

# Active states for the interface
active = {
    "Temperature": False,
    "Pressure": False,
    "Water Level": False,
}

sensor_values = {
    "Temperature": "25°C",
    "Pressure": "1013 hPa",
    "Water Level": "3 meters",
}

output_text = "Output will be displayed here."
path_to_font = None  # Define path_to_font as None

def update_sensor_value(sensor_name):
    """Update the sensor value with a random value."""
    if sensor_name == "Temperature":
        sensor_values[sensor_name] = f"{random.randint(15, 30)}°C"
    elif sensor_name == "Pressure":
        sensor_values[sensor_name] = f"{random.randint(1000, 1020)} hPa"
    elif sensor_name == "Water Level":
        sensor_values[sensor_name] = f"{random.randint(1, 5)} meters"

def frame_commands():
    global output_text
    gl.glClearColor(0.1, 0.1, 0.1, 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    io = imgui.get_io()

    if io.key_ctrl and io.keys_down[glfw.KEY_Q]:
        sys.exit(0)

    if imgui.begin_main_menu_bar():
        if imgui.begin_menu("File", True):
            clicked_quit, selected_quit = imgui.menu_item("Quit", False, True)

            if clicked_quit:
                sys.exit(0)

            imgui.end_menu()
        imgui.end_main_menu_bar()

    imgui.begin("Sensor Data")
    for label in active.copy().keys():
        if imgui.button(f"Show {label} Value"):
            active[label] = True
        imgui.same_line()
        if imgui.button(f"Update {label}"):
            update_sensor_value(label)
            output_text = f"{label} updated to {sensor_values[label]}"
    imgui.end()

    for label, enabled in active.copy().items():
        if enabled:
            imgui.begin(f"{label} Sensor")
            imgui.text(f"{label}: {sensor_values[label]}")
            imgui.end()

    # Output window
    imgui.begin("Output Window")
    imgui.text(output_text)
    imgui.end()

def render_frame(impl, window, font):
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
    width, height = 1200, 900
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
    font = io.fonts.add_font_from_file_ttf(path_to_font, 30) if path_to_font is not None else None
    impl.refresh_font_texture()

    while not glfw.window_should_close(window):
        render_frame(impl, window, font)

    impl.shutdown()
    glfw.terminate()

if __name__ == "__main__":
    main()
