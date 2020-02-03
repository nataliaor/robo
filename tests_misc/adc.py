

import pi2go2
from time import sleep

pi2go2.init(0)

try:
    while True:
        FL = pi2go2.getLightFL()
        FR = pi2go2.getLightFR()
        RL = pi2go2.getLightRL()
        RR = pi2go2.getLightRR()
        BAT = pi2go2.getBattery()
        print ("FL:%1.2f, FR:%1.2f, RL:%1.2f, RR:%1.2f, BAT:%1.1fV" % (FL,FR,RL,RR,BAT))
        sleep (1)

except KeyboardInterrupt:
    pass

finally:
    pi2go2.cleanup()
    
