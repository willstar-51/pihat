#!/usr/bin/env python
from sense_hat import SenseHat
import time
sense = SenseHat();

for i in range (1,255):
	sense.set_pixel(0,0,(90,0,0));
	time.sleep(0.5);
