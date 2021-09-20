# Change the colour of GlowBit LEDs using touch buttons.
# Requires a GlowBit rainbow or other device that uses WS2812Bv5 LEDs

import array, time
from machine import Pin
import rp2

from PiicoDev_CAP1203 import PiicoDev_CAP1203
from PiicoDev_Unified import sleep_ms # cross-platform-compatible sleep

touchSensor = PiicoDev_CAP1203(touchmode='multi', sensitivity=6) # Initialise in multi-touch mode so we can mix colours. Low sensitivity keeps away bugs

# Configure the number of WS2812 LEDs.
NUM_LEDS = 13
PIN_NUM = 22
brightness = 1


# WS2812B LED Driver code
##########################################################################
@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()


# Create the StateMachine with the ws2812 program, outputting on pin
sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))

# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)

# Display a pattern on the LEDs via an array of LED RGB values.
ar = array.array("I", [0 for _ in range(NUM_LEDS)])

##########################################################################


def pixels_show():
    dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
    for i,c in enumerate(ar):
        r = int(((c >> 8) & 0xFF) * brightness)
        g = int(((c >> 16) & 0xFF) * brightness)
        b = int((c & 0xFF) * brightness)
        dimmer_ar[i] = (g<<16) + (r<<8) + b
    sm.put(dimmer_ar, 8)
    time.sleep_ms(10)

def pixels_set(i, color):
    ar[i] = (color[1]<<16) + (color[0]<<8) + color[2]

def pixels_fill(color):
    for i in range(len(ar)):
        pixels_set(i, color)


while True:
    status = touchSensor.read()
    r = 255 * status[1] # Button 1 controls the red channel
    g = 255 * status[2] # Button 2 controls the green channel
    b = 255 * status[3] # Button 3 controls the blue channel
    pixels_fill( (r,g,b) ) # fill every LED with the RGB colour chosen
    pixels_show()
    if status[1] == 1:
        print("red ",end="")
    if status[2] == 1:
        print("green ",end="")
    if status[3] == 1:
        print("blue",end="")
    print("") # new line
    sleep_ms(100)
    