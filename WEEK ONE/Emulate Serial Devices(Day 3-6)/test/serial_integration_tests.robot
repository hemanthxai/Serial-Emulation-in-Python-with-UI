*** Settings ***
Library           SerialLibrary

*** Variables ***
${PORT_TEMPERATURE}    /dev/pts/8
${PORT_PRESSURE}       /dev/pts/11
${PORT_WATER_LEVEL}    /dev/pts/12
${BAUDRATE}            9600
${TIMEOUT}             1

*** Test Cases ***
Send Temperature Data
    Open Serial Port    ${PORT_TEMPERATURE}    ${BAUDRATE}    ${TIMEOUT}
    Write To Serial Port    25°C
    ${data}=    Read From Serial Port
    Should Be Equal As Strings    ${data}    25°C
    Close Serial Port

Send Pressure Data
    Open Serial Port    ${PORT_PRESSURE}    ${BAUDRATE}    ${TIMEOUT}
    Write To Serial Port    1013 hPa
    ${data}=    Read From Serial Port
    Should Be Equal As Strings    ${data}    1013 hPa
    Close Serial Port

Send Water Level Data
    Open Serial Port    ${PORT_WATER_LEVEL}    ${BAUDRATE}    ${TIMEOUT}
    Write To Serial Port    3 meters
    ${data}=    Read From Serial Port
    Should Be Equal As Strings    ${data}    3 meters
    Close Serial Port
