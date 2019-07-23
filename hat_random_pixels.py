#!/usr/bin/env python
import time
import random
from sense_hat import SenseHat
sense = SenseHat()
while 1:
	sense.clear()
	a = random.randint(0,255)
	b = random.randint(0,255)
	c = random.randint(0,255)
	x = random.randint(0,7)
	y = random.randint(0,7)
	sense.set_pixel(x,y,(a,b,c))
	time.sleep(0.05)
