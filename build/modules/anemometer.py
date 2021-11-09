from machine import ADC
from time import sleep_ms


class anemo:

    """
    0.4V -> 0 m/s (ideally)
    2.0V -> 32.4 m/s
    """

    def __init__(self, adc):
        self.adc = adc
        self.adc.atten(ADC.ATTN_11DB)  # 0.4V to 2.0V (max) 11dB -> 2.65V max (just in case)

    def _convert_ctoval(self, counts: int) -> float:
        volt = (counts / 8191) * 2.65  # 13 bit ADC -> 8192 = 2.65V
        return (32.4/1.6)*volt - 0.4


    def wind_speed(self) -> float:
        counts = self.adc.read()
        val1 = self._convert_ctoval(counts)
        sleep_ms(5)
        counts = self.adc.read()
        val2 = self._convert_ctoval(counts)
        sleep_ms(5)
        counts = self.adc.read()
        val3 = self._convert_ctoval(counts)
        return (val1, val2, val3)  # for m/s
#        c_mph = 2.236936
#        return (c_mph*val1, c_mph*val2, c_mph*val3)  # conversion of m/s to mph

    def update(self):
        items = self.wind_speed()
        out_str = "Anemometer: "
        for i in items:
            out_str += f"{i} "
        print(out_str)
        return items


