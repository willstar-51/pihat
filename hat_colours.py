#! /usr/bin/env python

from sense_hat import SenseHat
sense = SenseHat()

yellow = (66, 233, 245)
blue = (255,255,255)

speed = 0.05

message = "Hello World!";

sense.show_message(message, speed, text_colour=yellow)

sense.clear();
