# Pi2Go2 Wheel Sensor Test
# Moves: Forward, Reverse, spin Right, spin Left, Stop
# 20 pulses per revolution
# Press , . or < > to speed up slow down
# Press Ctrl-C to stop
#


import time
import pi2go2

# Reading single character by forcing stdin to raw mode
import sys
import tty
import termios

def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)  # 16=Up, 17=Down, 18=Right, 19=Left arrows

# End of single character reading

speed = 30

print("Tests the wheel sensors by using the arrow keys to control")
print("Use , or < to slow down")
print("Use . or > to speed up")
print("Speed changes take effect when the next arrow key is pressed")
print("Press Ctrl-C to end")


pi2go2.init(0)

# main loop
# change the number of counts to move or turn further
try:
    while True:
        keyp = readkey()
        if keyp == 'w' or ord(keyp) == 16:
            pi2go2.stepForward(speed, 20)  # Forward 20 counts
            print('Forward', speed)
        elif keyp == 'z' or ord(keyp) == 17:
            pi2go2.stepReverse(speed, 20)  # Reverse 20 counts
            print('Reverse', speed)
        elif keyp == 's' or ord(keyp) == 18:
            pi2go2.stepSpinR(speed, 20)  # Spin Right 20 counts
            print('Spin Right', speed)
        elif keyp == 'a' or ord(keyp) == 19:
            pi2go2.stepSpinL(speed, 20)  # Spin Left 20 counts
            print('Spin Left', speed)
        elif keyp == '.' or keyp == '>':
            speed = min(100, speed+10)
            print('Speed+', speed)
        elif keyp == ',' or keyp == '<':
            speed = max (0, speed-10)
            print('Speed-', speed)
        elif keyp == ' ':
            pi2go2.stop()
            print('Stop')
        elif keyp == '0':
            leftCount = 0
            rightCount = 0
        elif ord(keyp) == 3:
            break
        time.sleep(0.1)
        print("Left, Right:", pi2go2.countL, pi2go2.countR)

except KeyboardInterrupt:
    print

finally:
    pi2go2.cleanup()
    
