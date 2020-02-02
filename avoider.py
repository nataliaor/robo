#!/usr/bin/python
# Simple line Follower Program for Pi2Go 2

import pi2go2, time

pi2go2.init(0)

speed = 50

pi2go2.forward(speed)

# main loop
try:
  while True:
    dist = pi2go2.getDistance()
    if dist < 20:
      print (int(dist))
      pi2go2.reverse(speed)
      time.sleep(0.5)
      pi2go2.spinLeft(speed)
      time.sleep(0.5)
      pi2go2. forward(speed)
    time.sleep(0.01)

except KeyboardInterrupt:
       pi2go2.cleanup()
