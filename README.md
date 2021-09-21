# PiicoDev® Capacitive Touch Sensor CAP1203 MicroPython Module

This is the firmware repo for the [Core Electronics PiicoDev® Capacitive Touch Sensor CAP1203](https://core-electronics.com.au/catalog/product/view/sku/CE07816)

This module depends on the [PiicoDev Unified Library](https://github.com/CoreElectronics/CE-PiicoDev-Unified), include `PiicoDev_Unified.py` in the project directory on your MicroPython device.

<!-- TODO update tutorial link with the device tinyurl eg. piico.dev/p1
See the [Quickstart Guide](https://piico.dev/pX)
 -->

# Usage
## Example
[main.py](https://github.com/CoreElectronics/CE-PiicoDev-CAP1203-MicroPython-Module/blob/main/main.py) is a simple example to get started.
```
# PiicoDev Capacitive Touch Sensor CAP1203 demo code
# Read the touch sensor buttons and print the result

from PiicoDev_CAP1203 import PiicoDev_CAP1203
from PiicoDev_Unified import sleep_ms # cross-platform-compatible sleep

touchSensor = PiicoDev_CAP1203()

while True:
   # Example: Display touch-pad statuses
   status = touchSensor.read()
   print("Touch Pad Status: " + str(status[1]) + "  " + str(status[2]) + "  " + str(status[3]))

   sleep_ms(100)
```
## Details
### `PiicoDev_CAP1203(bus=, freq=, sda=, scl=, addr=0x28, touchmode='multi', sensitivity=3)`
Parameter | Type | Range | Default | Description
--- | --- | --- | --- | ---
bus | int | 0,1 | Raspberry Pi Pico: 0, Raspberry Pi: 1 | I2C Bus.  Ignored on Micro:bit
freq | int | 100-1000000 | Device dependent | I2C Bus frequency (Hz).  Ignored on Raspberry Pi
sda | Pin | Device Dependent | Device Dependent | I2C SDA Pin. Implemented on Raspberry Pi Pico only
scl | Pin | Device Dependent | Device Dependent | I2C SCL Pin. Implemented on Raspberry Pi Pico only
addr | int | 0x28 | 0x28 | This address cannot be changed
touchmode | string | 'single' / 'multi' | 'multi' | 'single': allow only one touch pad to operate at one time. 'multi': allow multiple touches at the same time
sensitivity | int | 0 - 7 | 0: Highest Sensitivity, 7: Minimum Sensitivity | Selects the sensitivity of the touch sensor.

### `PiicoDev_CAP1203.read()`
Returns a dictionary with the status of each touch pad.

Parameter | Type | Description
--- | --- | ---
1 | int | Touch pad 1 reading
2 | int | Touch pad 2 reading
3 | int | Touch pad 3 reading

### `PiicoDev_CAP1203.readDeltaCounts()`
Returns  a dictionary with the raw reading of each touch pad.

Parameter | Type | Description
--- | --- | ---
1 | int | Touch pad 1 reading
2 | int | Touch pad 2 reading
3 | int | Touch pad 3 reading


# License
This project is open source - please review the LICENSE.md file for further licensing information.

If you have any technical questions, or concerns about licensing, please contact technical support on the [Core Electronics forums](https://forum.core-electronics.com.au/).

*\"PiicoDev\" and the PiicoDev logo are trademarks of Core Electronics Pty Ltd.*
