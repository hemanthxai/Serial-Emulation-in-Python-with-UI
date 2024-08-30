sudo socat -d -d PTY,link=/dev/ttyS1,raw,echo=0 PTY,link=/dev/ttyS2,raw,echo=0 &
sudo socat -d -d PTY,link=/dev/ttyS3,raw,echo=0 PTY,link=/dev/ttyS4,raw,echo=0 &
sudo socat -d -d PTY,link=/dev/ttyS5,raw,echo=0 PTY,link=/dev/ttyS6,raw,echo=0 &
