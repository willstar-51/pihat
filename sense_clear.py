#! /usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()


print("clearing LEDs");

sense.clear();

sense.show_message("Hello world!")
