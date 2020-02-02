#!/usr/bin/python
# Simple line Follower Program for Pi2Go 2

import pi2go2, time

pi2go2.init(0)

slowspeed = 20
fastspeed = 40

lastleft = 0
lastright = 0

# Let's get going
#pi2go2.forward(fastspeed)

# main loop
try:
  while True:
    left = pi2go2.irLeftLine()
    right = pi2go2.irRightLine()
    print "Left, Right", left, right
    time.sleep(1)

except KeyboardInterrupt:
       pi2go2.cleanup()
