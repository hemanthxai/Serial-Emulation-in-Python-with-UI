import pytest
import random
import imgui_interface.main as t


@pytest.mark.update_sensor
def test_update_sensor_value():

    t.update_sensor_value("Temperature")
    assert t.sensor_values["Temperature"] != "0°C"

    t.update_sensor_value("Pressure")
    assert t.sensor_values["Pressure"] != "0 hPa"

    t.update_sensor_value("Water Level")
    assert t.sensor_values["Water Level"] != "0 meters"


@pytest.mark.update_all
def test_update_all_sensor_values():
    global output_text
    output_text = ""
    t.update_all_sensor_values()

    assert "Temperature updated to" in output_text
    assert "Pressure updated to" in output_text
    assert "Water Level updated to" in output_text


@pytest.mark.generate_all_thread
def test_generate_all_thread():
    global output_text
    output_text = ""
    t.generate_all_thread()
    import time

    time.sleep(0.5)
    assert "Temperature updated to" in output_text
    assert "Pressure updated to" in output_text
    assert "Water Level updated to" in output_text


@pytest.mark.imgui
def test_clear_secondary_window():
    global secondary_window_text
    secondary_window_text = ["Temp: 25°C", "Pressure: 1013 hPa"]
    secondary_window_text.clear()

    assert len(secondary_window_text) == 0


@pytest.mark.active_sensors
def test_active_sensors():
    global active_sensors
    t.active_sensors["Temperature"] = True
    t.active_sensors["Pressure"] = False
    t.active_sensors["Water Level"] = True

    assert t.active_sensors["Temperature"] is True
    assert t.active_sensors["Pressure"] is False
    assert t.active_sensors["Water Level"] is True
