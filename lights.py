import machine, neopixel, time

#states
OFF = 0
STATIC = 1
MARQUEE = 2
FADE = 3

class Lights():

    def __init__(self, pin, led_count):
        self.pin = pin
        self.led_count = led_count
        self.np = neopixel.NeoPixel(machine.Pin(pin), led_count)

        self.state = OFF
        self.colors = []
        self.interval = 0.5

    def run(self):
        if self.state == OFF:
            self.clear()
            time.sleep(1)
            return
        elif self.state == STATIC:
            self.static()
            return
        elif self.state == MARQUEE:
            self.marquee()
            return
        elif self.state == FADE:
            self.fade()
            return
        
    def clear(self, color=None):
        if not color:
            color = (0,0,0)

        for i in range(self.led_count):
            self.np[i] = color
        self.np.write()

    def dimByFactor(self, color, factor):
        return tuple([int(c*factor) for c in color])

    def static(self):
        if len(self.colors) == 0:
            time.sleep(1)
            return

        for i in range(self.led_count):
            self.np[i] = self.colors[i % len(self.colors)]
        self.np.write()

    def marquee(self):
        if len(self.colors) == 0:
            time.sleep(1)
            return

        for offset in range(len(self.colors)):
            for i in range(self.led_count):
                self.np[i] = self.colors[(i + offset) % len(self.colors)]
            self.np.write()
            time.sleep(self.interval)
    
    def fade(self):
        for color in self.colors:
            gradient = [ color ]

            while gradient[-1][0] > 0 or gradient[-1][1] > 0 or gradient[-1][2] > 0:
                gradient.append(self.dimByFactor(gradient[-1], 0.9))

            for g in reversed(gradient):
                self.clear(g)
                time.sleep(self.interval)

            for g in gradient:
                self.clear(g)
                time.sleep(self.interval)




