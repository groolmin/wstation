# ESP32-S2 Micropython Weather Station
bmp180.py is from [here](https://github.com/micropython-IMU/micropython-bmp180)
## Current Implementation
Provides an Access Point (AP) for the user to connect to via their phone.
Once connected the user can go to 192.168.4.1 (default socket) to get the two current metrics (pressure sensor, anemometer, 8 position wind vane)
## Anemometer
0.4 to 2.0V matching 0 to 32.4 m/s respectively.
ADC attenuation of 11DB allows for about 2.7V with 13 bit width (tested at 9V)
## Wind Vane (Direction Sensor)
8 directions (North, North-East, East, etc.) each direction corresponding to a voltage level.
Tested with 12V (shows all 8 voltage levels) and to go within ADC bounds a voltage divider is setup to half the seen-ADC-voltage. Example: two 100 ohm resistors, one in series with the incoming direction signal, and another between signal and ground.
