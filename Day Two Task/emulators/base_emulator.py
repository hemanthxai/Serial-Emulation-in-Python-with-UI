import threading
import queue
from protobuf_definitions.device_pb2 import DeviceCommand, DeviceResponse


class BaseEmulator(threading.Thread):
    def __init__(self, command_queue: queue.Queue, response_queue: queue.Queue):
        super().__init__()
        self.command_queue = command_queue
        self.response_queue = response_queue
        self.running = True

    def run(self):
        while self.running:
            try:
                command = self.command_queue.get(timeout=1)
                response = self.process_command(command)
                self.response_queue.put(response)
            except queue.Empty:
                continue

    def process_command(self, command: DeviceCommand) -> DeviceResponse:
        raise NotImplementedError

    def stop(self):
        self.running = False
