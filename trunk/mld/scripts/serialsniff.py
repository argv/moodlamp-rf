 # Copyright (c) 2008 by Tobias Schneider <schneider@blinkenlichts.net>
 # Copyright (c) <year> by your name <your@email>
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # any later version.
 #
 # This program is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License
 # along with this program.  If not, see <http://www.gnu.org/licenses/>.


import threading
import serial
import string
import curses
import sys
import time
import math
import random

ser =  serial.Serial('/dev/ttyUSB1', 230400)

data = []
#ser.write(aus)
escaped = False
stop = False
start = False

while True:
    c = ser.read(1)
#    print "c=", c
#    continue
    if escaped:
        if c == 'c':
            start = True
        elif c == 'b':
            stop = True
        elif c == 'a':
            d = 'a'
        escaped = False
    elif c == 'a':
        escaped = 1
    else:
        d = c
        
    if start:
        start = False
    elif stop:
        print time.time(), len(data) ,data
        data = []
        stop = False
    elif escaped == False:
        data.append(d)
        
    

