from machine import ADC


class wind_vane():

    def __init__(self, adc):
        self.adc = adc
        self.adc.atten(ADC.ATTN_11DB)

    _bound = 150

    _directions = {
            1200: 'N',
            1900: 'NE',
            2600: 'E',
            3300: 'SE',
            4000: 'S',
            4700: 'SW',
            5400: 'W',
            6100: 'NW'
    }


    def read_direction(self) -> str:
        val = self.adc.read()
        for d in self._directions:
            if ((val >= d-self._bound) and (val < d+self._bound)):
                return self._directions[d]
        return None  # if not found

    def update(self):
        d = self.read_direction()
        if d != None:
            return d
        else: return "Error"

