import time
import pi2go2

pi2go2.init(0)

try:
    while True:
        dist = pi2go2.getDistance()
        print ("Distance 0: ", int(dist))
        dist = pi2go2.getDistance(pi2go2.sonar1)
        print ("Distance 1: ", int(dist))
        print ()
        time.sleep(1)

except KeyboardInterrupt:
    print
    pass

finally:
    pi2go2.cleanup()
