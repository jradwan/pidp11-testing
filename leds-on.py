# LEDs-On 
# Jeremy C. Radwan
# April 9, 2019
#
# This simple Python script loops through the GPIO pins that control the 
# PiDP-11's 6 LED rows and 12 LED columns and toggles them appropriately
# to turn on all of the LEDs. 
#
# Modification History:
#
# (05/18/2019, JCR) - corrected GPIO/pin confusion in ledrows and ledcols
#                     arrays; consolidated GPIO statements

import RPi.GPIO as GPIO  

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print "\nTurning on all PiDP-11 LEDs ...\n"

# ledrows (xled0-5) associated gpio pins
# NOTE: these pin numbers correspond not to the PHYSICAL pin numbers, but the gX numbers listed on the schematic)
#       example: xled5 = g25 = pin 22
ledrows = [20, 21, 22, 23, 24, 25]

# turn on ledrows
rowcount = 0
for row in ledrows:
  print "Turning on xled" + str(rowcount) + " (pin " + str(row) + ")"
  rowcount = rowcount + 1
  GPIO.setup(row, GPIO.OUT, initial = GPIO.HIGH)

print ""

# ledcols (col0-11) associated gpio pins
# NOTE: these pin numbers correspond not to the PHYSICAL pin numbers, but the gX numbers listed on the schematic)
#       example: col0 = g26 = pin 37
ledcols = [26, 27, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# turn on ledcols
colcount = 0
for col in ledcols:
  print "Turning on col" + str(colcount) + " (pin " + str(col) + ")"
  colcount = colcount + 1
  GPIO.setup(col, GPIO.OUT, initial = GPIO.LOW)

print "\nDone!\n"
