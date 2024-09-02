import unittest
from unittest.mock import patch
import random
import threading
import imgui


from imgui_interface.main import *
class TestSensorFunctions(unittest.TestCase):
    
    @patch('random.randint')
    def test_update_sensor_value(self, mock_randint):

        mock_randint.return_value = 30
        update_sensor_value("Temperature")
        self.assertEqual(sensor_values["Temperature"], "30°C")


        mock_randint.return_value = 1015
        update_sensor_value("Pressure")
        self.assertEqual(sensor_values["Pressure"], "1015 hPa")


        mock_randint.return_value = 3
        update_sensor_value("Water Level")
        self.assertEqual(sensor_values["Water Level"], "3 meters")

    @patch('random.randint')
    def test_update_all_sensor_values(self, mock_randint):

        mock_randint.side_effect = [25, 1000, 2]  

        update_all_sensor_values()

        expected_output = (
            "Temperature updated to 25°C\n"
            "Pressure updated to 1000 hPa\n"
            "Water Level updated to 2 meters\n"
        )
        self.assertEqual(output_text, expected_output)
        self.assertEqual(sensor_values["Temperature"], "25°C")
        self.assertEqual(sensor_values["Pressure"], "1000 hPa")
        self.assertEqual(sensor_values["Water Level"], "2 meters")

    @patch('your_module.update_all_sensor_values')
    def test_generate_all_thread(self, mock_update_all):
        # Start the thread
        generate_all_thread()

        # Ensure the thread runs the update_all_sensor_values function
        mock_update_all.assert_called_once()

if __name__ == '__main__':
    unittest.main()
