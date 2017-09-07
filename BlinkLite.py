# Author: N. G. Peters
# date: 31Aug2017
# class: Python/Pi
# purpose: To plot some functions
# input: - specify a function in the myFunction function function
#        - specify unterval length and number of plotting points
# output: - plot a function with a title and labels
#
#===================================================================

# imports
import math # for PI, sines, cosines, etc
import sys # for a graceful exit
import os # to check if a datafile exists 
from pylab import plot, show, title, xlabel, ylabel, legend, savefig, grid, scatter
from pylab import xlim, ylim 
import time
import RPi.GPIO as GPIO







# define global constants and Booleans
DEBUG = False
#DEBUG = True
led_ye = 6 # pin 31
led_re = 19 # pin 35
led_bl = 26 # pin 37
led_gr = 21 # pin 40
time2sleep =.02

t=0

# define functions 


# ===== Main Program =====
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_re,GPIO.OUT)
GPIO.setup(led_ye,GPIO.OUT)
GPIO.setup(led_bl,GPIO.OUT)
GPIO.setup(led_gr,GPIO.OUT)


x=.2
while True:
    t+=3.1415*x
    x=.01*math.sin(t) +.011
    time2sleep =x
    GPIO.output(led_ye,GPIO.HIGH)
    time.sleep(time2sleep)
    GPIO.output(led_ye,GPIO.LOW)
    time.sleep(time2sleep)
    GPIO.output(led_gr,GPIO.HIGH)
    time.sleep(time2sleep)
    GPIO.output(led_gr,GPIO.LOW)
    time.sleep(time2sleep)
    GPIO.output(led_re,GPIO.HIGH)
    time.sleep(time2sleep)
    GPIO.output(led_re,GPIO.LOW)
    time.sleep(time2sleep)
    GPIO.output(led_bl,GPIO.HIGH)
    time.sleep(time2sleep)
    GPIO.output(led_bl,GPIO.LOW)


#form plots





print('\n-- End of program --')



