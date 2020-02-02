#!/usr/bin/python
# Simple line Follower Program for Pi2Go 2

import pi2go2, time

pi2go2.init(0)



slowspeed = 10
fastspeed = 25

lastleft = 0
lastright = 0

pi2go2.forward(fastspeed)

# main loop
try:
  while True:
    left = pi2go2.irLeftLine()
    right = pi2go2.irRightLine()
    if not left and not right:
      pi2go2.stop()
    if not left and lastleft:
      pi2go2.brake()
      print("Left")
      pi2go2.spinLeft(slowspeed)
      while not pi2go2.irLeftLine():
        time.sleep(0.01)
      time.sleep(0.1)
    elif not right and lastright:
      pi2go2.brake()
      print("Right")
      pi2go2.spinRight(slowspeed)
      while not pi2go2.irRightLine():
        time.sleep(0.01)
      time.sleep(0.1)
    else:
      pi2go2.forward(fastspeed)
    lastleft = left
    lastright = right
    time.sleep(0.01)

except KeyboardInterrupt:
       pi2go2.cleanup()
