*** Settings ***
Library           SerialLibrary

*** Test Cases ***
Test Serial Communication
    Open Serial Port    /dev/ttyS1
    Write To Serial Port    example_command
    ${response}=    Read From Serial Port
    Should Contain    ${response}    Processed by Device 1
    Close Serial Port
