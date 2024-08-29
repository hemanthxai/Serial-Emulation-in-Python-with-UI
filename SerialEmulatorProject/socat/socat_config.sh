#!/bin/bash

# Create virtual serial ports
socat -d -d pty,link=/dev/ttyS1,raw,echo=0 pty,link=/dev/ttyS2,raw,echo=0 &
socat -d -d pty,link=/dev/ttyS3,raw,echo=0 pty,link=/dev/ttyS4,raw,echo=0 &
