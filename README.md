# PiDP-11 Test Utilities

Just some quick utilities I threw together to test my PiDP-11 kit (similar to what I did for my [PiDP-8](https://github.com/jradwan/pidp8-testing)). Check out my construction time-lapse video [here](https://www.youtube.com/watch?v=HMgWKK6EIEk)!

#### [LEDS-OFF](https://github.com/jradwan/pidp11-testing/blob/master/leds-off.py) ####

Sometimes during my testing I've had random LEDs get stuck on. This simple Python script turns OFF all of the LEDs.

#### [LEDS-ON](https://github.com/jradwan/pidp11-testing/blob/master/leds-on.py) ####

Counterpart to LEDS-OFF, this simple Python script turns ON all of the LEDs.

#### [LED-CONTROL](https://github.com/jradwan/pidp11-testing/blob/master/led-control.py) ####

After initially creating LEDS-OFF and LEDS-ON, it made sense to combine them into a single script with a command-line switch to determine if the LEDs should be turned on or off.
