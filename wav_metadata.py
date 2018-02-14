#!/usr/bin/python

import math
import wave
import struct
import contextlib

text_file = open("spanish.txt",'r')
file2 = open("durations2.txt","w")
lines = text_file.read().splitlines()

y = len(lines)
x = 0
for x in range(0,y):
	with contextlib.closing(wave.open(lines[x],'r')) as f:
		
		frames = f.getnframes()
		rate = f.getframerate()
		duration = (frames / float(rate))*1000
		duration = format(duration, '.0f')
		print(lines[x],duration)
		file2.write(lines[x] + " " + duration + " \n")
	 	
file2.close()
text_file.close()
