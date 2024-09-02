from base_emulator import BaseEmulator
from protobuf_definitions import DeviceCommand, DeviceResponse


class Device1Emulator(BaseEmulator):
    def process_command(self, command: DeviceCommand) -> DeviceResponse:
        response = DeviceResponse()
        response.result = "Processed by Device 1"
        return response
