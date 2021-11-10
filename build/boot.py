import esp
# mute vendor O/S debugging messages on UART
esp.osdebug(None)
esp.osdebug(0)

from machine import Pin, SoftI2C, ADC
from modules.anemometer import anemo
from modules.bmp180 import BMP180
from modules.vane import wind_vane
from modules.esp_ap import APWebserver


def sensor_init() -> list:
    """
    Software I2C - Pin 4, Pin 5
    ADC (Anemometer) - Pin 1
    """
    i2c = SoftI2C(scl=Pin(4), sda=Pin(5), freq=400000)
    adc1 = ADC(Pin(1))
    adc2 = ADC(Pin(2))
    a = anemo(adc1)
    b = BMP180(i2c)
    d = wind_vane(adc2)
    return [a,b,d]

def update_sensors(sensors: list) -> list:
    out = []
    for sensor in sensors:
        out.append(sensor.update())
    return out


def main_thread() -> None:
    sensor_list = sensor_init()
    ap = APWebserver('ROCKERT', 'SP0KAN3', '192.168.1.2')

    while(True):
        try:
            buffers = update_sensors(sensor_list)
            print("Buffers updated, waiting for response from client")
            ap.wait_connection(buffers)
            print("Sent to client")
        except KeyboardInterrupt:
            print("Stopping for REPL")
            break


if __name__ == "__main__":
    main_thread()
