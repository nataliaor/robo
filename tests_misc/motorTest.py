# Pi2Go2 Motor Test
# Moves: Forward, Reverse, turn Right, turn Left, Stop 
# Press Ctrl-C to stop
#
# To check wiring is correct ensure the order of movement as above is correct


import pi2go2, time

#======================================================================
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
#======================================================================

speed = 100

print("Tests the motors by using the arrow keys to control")
print("Use , or < to slow down")
print("Use . or > to speed up")
print("Speed changes take effect when the next arrow key is pressed")
print("Press space bar to coast to stop")
print("Press b to brake and stop quickly")
print("Press Ctrl-C to end")


pi2go2.init(10)

# main loop
try:
    while True:
        keyp = readkey()
        if keyp == 'w' or ord(keyp) == 16:
            pi2go2.forward(speed)
            print('Forward', speed)
        elif keyp == 'z' or ord(keyp) == 17:
            pi2go2.reverse(speed)
            print('Reverse', speed)
        elif keyp == 's' or ord(keyp) == 18:
            pi2go2.spinRight(speed)
            print('Spin Right', speed)
        elif keyp == 'a' or ord(keyp) == 19:
            pi2go2.spinLeft(speed)
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
        elif keyp == 'b':
            pi2go2.brake()
            print('Brake')
        elif ord(keyp) == 3:
            break

except KeyboardInterrupt:
    pass

finally:
    pi2go2.cleanup()
    
