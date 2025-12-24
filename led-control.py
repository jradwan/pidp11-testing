# LED-Control
# Jeremy C. Radwan
# May 18, 2019
#
# This Python script is a consolidation of LEDs-Off and LEDs-On.
#
# Modification History:
#
# (2025-12-23, JCR) - updated for python3 (replaced <> with !=, used print(), etc.)
#

import RPi.GPIO as GPIO
import sys

CMD_HELP = "\nLED-Control syntax: python led-control.py on|off [-v (for verbose messages)]\n"
debug = False

# ledrows (xled0-5) associated gpio pins
# NOTE: these numbers correspond not to the PHYSICAL pin numbers, but the gX numbers listed on the schematic)
#       example: xled5 = g25 = pin 22
ledrows = [20, 21, 22, 23, 24, 25]

# ledcols (col0-11) associated gpio pins
# NOTE: these numbers correspond not to the PHYSICAL pin numbers, but the gX numbers listed on the schematic)
#       example col0 = g26 = pin 37
ledcols = [26, 27, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# check command-line arguments
if len(sys.argv) != 1:
  if str.lower(sys.argv[1]) == "on":
    action = "on"
    gpio_row = GPIO.HIGH
    gpio_col = GPIO.LOW
  elif str.lower(sys.argv[1]) == "off":
    action = "off"
    gpio_row = GPIO.LOW
    gpio_col = GPIO.HIGH
  else:
    sys.exit(CMD_HELP)

  if len(sys.argv) == 3:
    if str.lower(sys.argv[2]) == "-v":
      debug = True
    else:
      sys.exit(CMD_HELP)
else:
  sys.exit(CMD_HELP)

if debug:
  print(f'\nTurning {action} all PiDP-11 LEDs ...\n')

# act on ledrows
rowcount = 0
for row in ledrows:
  if debug:
    print(f'Turning {action} xled {rowcount=} (pin {row=})')
  rowcount = rowcount + 1
  GPIO.setup(row, GPIO.OUT, initial = gpio_row)

if debug:
  print(f'')

# act on ledcols
colcount = 0
for col in ledcols:
  if debug:
    print(f'Turning {action} col {colcount=} (pin {col=})')
  colcount = colcount + 1
  GPIO.setup(col, GPIO.OUT, initial = gpio_col)

if debug:
  print(f'\nDone!\n')
  
