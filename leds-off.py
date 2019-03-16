# LEDs-Off
# Jeremy C. Radwan
# March 14, 2019
#
# This simple Python script loops through the GPIO pins that control
# the PiDP-11's 6 LED rows and 12 LED columns and toggles them to HIGH
# to shut off all LEDs. Useful for "clearing" the from panel of any 
# "stuck" LEDs after exiting from simh.
#
# Modification History:
#

import RPi.GPIO as GPIO  

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

print "\nTurning off all PiDP-11 LEDs ...\n"

# ledrows (0-5) associated gpio pins
ledrows = [38, 40, 15, 16, 18, 22]

# turn off ledrows
rowcount = 0
for row in ledrows:
  print "Turning off xled" + str(rowcount) + " (pin " + str(row) + ")"
  rowcount = rowcount + 1
  GPIO.setup(row, GPIO.OUT)
  GPIO.output(row, GPIO.HIGH)

print ""

# ledcols (0-11) associated gpio pins
ledcols = [37, 13, 7, 29, 31, 26, 24, 21, 19, 23, 32, 33]

# turn off ledcols
colcount = 0
for col in ledcols:
  print "Turning off col" + str(colcount) + " (pin " + str(col) + ")"
  colcount = colcount + 1
  GPIO.setup(col, GPIO.OUT)
  GPIO.output(col, GPIO.HIGH)

print "\nDone!"

# cleanup and exit
GPIO.cleanup()
