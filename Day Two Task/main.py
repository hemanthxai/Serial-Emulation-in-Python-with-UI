import queue
import threading
import time
from emulators.device1_emulator import Device1Emulator
from ui.imgui_interface import render_ui
from config.config import load_config


def main():
    # Load configuration
    config = load_config("config/config.yaml")

    # Create queues for communication
    command_queue = queue.Queue()
    response_queue = queue.Queue()

    # Initialize and start emulators
    emulators = []
    for emulator_config in config.emulators:
        if emulator_config["type"] == "device1":
            emulator = Device1Emulator(command_queue, response_queue)
            emulators.append(emulator)
            emulator.start()

    try:
        # Main loop for the UI
        while True:
            # Render the UI
            render_ui(command_queue, response_queue)
            time.sleep(0.1)  # Adjust sleep time as needed for performance

    except KeyboardInterrupt:
        # Stop emulators on exit
        for emulator in emulators:
            emulator.stop()
        for emulator in emulators:
            emulator.join()


if __name__ == "__main__":
    main()
