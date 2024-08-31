import unittest
from unittest.mock import patch, MagicMock
import random
import threading
from imgui_interface.main import update_sensor_value, update_all_sensor_values, generate_all_thread, active_sensors, sensor_values, output_text, secondary_window_text


@pytest.fixture
def app():
    return SensorApp()

@patch('random.randint')
def test_update_sensor_value(mock_randint, app):
    # Test Temperature
    mock_randint.return_value = 30
    app.update_sensor_value("Temperature")
    assert app.sensor_values["Temperature"] == "30°C"

    # Test Pressure
    mock_randint.return_value = 1015
    app.update_sensor_value("Pressure")
    assert app.sensor_values["Pressure"] == "1015 hPa"

    # Test Water Level
    mock_randint.return_value = 3
    app.update_sensor_value("Water Level")
    assert app.sensor_values["Water Level"] == "3 meters"

@patch('random.randint')
def test_update_all_sensor_values(mock_randint, app):
    # Set mock return values
    mock_randint.side_effect = [25, 1000, 2]  # Values for Temperature, Pressure, and Water Level

    app.update_all_sensor_values()

    expected_output = (
        "Temperature updated to 25°C\n"
        "Pressure updated to 1000 hPa\n"
        "Water Level updated to 2 meters\n"
    )
    assert app.output_text == expected_output
    assert app.sensor_values["Temperature"] == "25°C"
    assert app.sensor_values["Pressure"] == "1000 hPa"
    assert app.sensor_values["Water Level"] == "2 meters"

def test_generate_all_thread(app):
    with patch.object(app, 'update_all_sensor_values') as mock_update_all:
        app.generate_all_thread()
        # Ensure the function is called in a thread
        mock_update_all.assert_called_once()

if __name__ == '__main__':
    pytest.main()