# Test program for Pi2Go Mk2 Smart RGB LEDs

import pi2go2, time

numLEDs = pi2go2.numPixels
RED = pi2go2.fromRGB(255,0,0)
ORANGE = pi2go2.fromRGB(255,255,0)
GREEN = pi2go2.fromRGB(0,255,0)
BLUE = pi2go2.fromRGB(0,0,255)
BLACK = pi2go2.fromRGB(0,0,0)
WHITE = pi2go2.fromRGB(255,255,255)

pi2go2.init(40)

try:
    while True:
        pi2go2.rainbow()
        pi2go2.show()
        time.sleep(10)
        pi2go2.clear()
        pi2go2.show()
        time.sleep(0.5)

except KeyboardInterrupt:
    print

try:
    pi2go2.cleanup()
except Exception as e:
    print (e)
