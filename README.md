# ESP32-S2 Micropython Weather Station
This repository contains the build, documentation and setup of a simple weather station built on an ESP32-S2 with micropython.
## REPL and Build Resources
1. Download rshell
 - `sudo apt install rshell`
2. Download repository
 - `git clone https://github.com/groolmin/wstation.git`
## ESP32 micropython setup
1. Download esptool.py to flash micropython build esp12k_1.17_fb_boost_4M.bin (provided [here](https://github.com/wangshujun-tj/mpy-Framebuf-boost/blob/main/esp12k_1.17_fb_boost_4M.bin))
 - `python -m pip install esptool`
2. Erase remaining flash on the ESP32-S2
 - `esptool.py --chip esp32s2 --port /dev/<port> erase_flash` (for me <port> is ttyUSB0)
3. Write micropython binary to flash
 - `esptool.py --chip esp32s2 --port /dev/<port> write_flash -z 0x1000 esp12k_1.17_fb_boost_4M.bin`
## Copy Build to Flash
1. `rshell -p /dev/<port>`
2. `cd wstation`
3. `rshell cp -r build/* /pyboard/`
Build is all set, you can enter REPL to debug in rshell with `repl` and reboot with CTRL+D

