sudo socat -d -d PTY,link=/dev/a1,raw,echo=0 PTY,link=/dev/a2,raw,echo=0 &
sudo socat -d -d PTY,link=/dev/b1,raw,echo=0 PTY,link=/dev/b2,raw,echo=0 &
sudo socat -d -d PTY,link=/dev/c1,raw,echo=0 PTY,link=/dev/c2,raw,echo=0 &
