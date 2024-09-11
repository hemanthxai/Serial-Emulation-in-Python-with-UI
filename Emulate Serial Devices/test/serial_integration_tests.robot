*** Settings ***
Library    OperatingSystem
Library    Process
Library    Collections
Suite Setup    Start Application
Suite Teardown    Terminate Application

*** Variables ***
${COMMAND}    python
${SCRIPT}     main.py
${TIMEOUT}    10 seconds

*** Test Cases ***
Test Sensor Value Updates
    [Documentation]    Verify that sensor values are updated correctly.
    Call Method    update_sensor_value    Temperature
    ${temp_val}    Evaluate    ${sensor_values["Temperature"]} != "0°C"
    Should Be True    ${temp_val}

    Call Method    update_sensor_value    Pressure
    ${press_val}    Evaluate    ${sensor_values["Pressure"]} != "0 hPa"
    Should Be True    ${press_val}

    Call Method    update_sensor_value    Water Level
    ${water_val}    Evaluate    ${sensor_values["Water Level"]} != "0 meters"
    Should Be True    ${water_val}

Test Generate All Sensors
    [Documentation]    Test the 'Generate All' functionality.
    Run Process    python    -c    from main import generate_all_thread; generate_all_thread()
    ${output_text}    Get Output    result
    Should Contain    ${output_text}    Temperature updated to
    Should Contain    ${output_text}    Pressure updated to
    Should Contain    ${output_text}    Water Level updated to

*** Keywords ***
Start Application
    [Documentation]    Start the ImGui application.
    Start Process    ${COMMAND}    ${SCRIPT}

Terminate Application
    [Documentation]    Terminate the ImGui application.
    Terminate All Processes
