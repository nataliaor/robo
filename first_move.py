import gpiozero
import time
import pi2go2



pi2go2.init(100)


robot =gpiozero.Robot(left=(17,18),right=(27,22))

for i in range(10):
	robot.forward()
	time.sleep(0.5)


	robot.left()
	time.sleep(0.5)
