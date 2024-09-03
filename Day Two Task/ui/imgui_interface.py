import imgui
import numpy as np
from protobuf_definitions import DeviceResponse
import queue


def plot_live_data(response_queue: queue.Queue):
    # Dummy function for plotting data
    # Replace with actual plotting logic using ImGui
    while True:
        try:
            response = response_queue.get(timeout=1)
            # Process and plot response data
        except queue.Empty:
            break


def render_ui(command_queue: queue.Queue, response_queue: queue.Queue):
    imgui.new_frame()

    imgui.begin("Live Data Plot")
    plot_live_data(response_queue)
    imgui.end()

    imgui.begin("Control Panel")
    if imgui.button("Send Command"):
        command = DeviceCommand()
        command.command = "example_command"
        command_queue.put(command)

    slider_value = imgui.slider_float("Slider", 0.0, 1.0, 0.5)
    imgui.end()

    imgui.render()
