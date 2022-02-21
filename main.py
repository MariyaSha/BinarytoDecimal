from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty

class ScreenX(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.toolbar = ObjectProperty(None)
        self.input = ObjectProperty(None)
        self.label = ObjectProperty(None)
        self.converted = ObjectProperty(None)
        self.state = 0

    def flip(self):
        # a method for the "flip" icon
        # changes the state of the app
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Decimal to Binary"
            self.input.hint_text = "enter a decimal number"
        else:
            self.state = 0
            self.toolbar.title = "Binary to Decimal"
            self.input.hint_text = "enter a binary number"
        # hide labels until needed
        self.converted.text = ""
        self.label.text = ""

    def convert(self):
        # a method to find the decimal/binary equivalent
        try:
            if "." not in self.input.text:
                # if the user-provided number is not a fraction
                if self.state == 0:
                    # binary to decimal
                    val = str(int(self.input.text, 2))
                    self.label.text = "in decimal is:"
                else:
                    # decimal to binary
                    val = bin(int(self.input.text))[2:]
                    self.label.text = "in binary is:"
                self.converted.text = val
            else:
                # if the user provided number is a fraction
                whole, fract = self.input.text.split(".")

                if self.state == 0:
                    # convert binary to decimal
                    whole = int(whole, 2)
                    floating = 0
                    for idx, digit in enumerate(fract):
                        floating += int(digit) * 2 ** (-(idx + 1))
                    self.label.text = "in decimal is:"
                    self.converted.text = str(whole + floating)
                else:
                    # convert decimal to binary
                    decimal_places = 10
                    whole = bin(int(whole))[2:]
                    fract = float("0." + fract)
                    floating = []
                    for i in range(decimal_places):
                        if fract * 2 < 1:
                            floating.append("0")
                            fract *= 2
                        elif fract * 2 > 1:
                            floating.append("1")
                            fract = fract * 2 - 1
                        elif fract * 2 == 1.0:
                            floating.append("1")
                            break
                    self.label.text = "in binary is:"
                    self.converted.text = whole + "." + "".join(floating)
        except ValueError:
            # if the user-provided value is invalid
            self.converted.text = ""
            if self.state == 0:
                # binary to decimal
                self.label.text = "please enter a valid binary number"
            else:
                # decimal to binary
                self.label.text = "please enter a valid decimal number"


class MainApp(MDApp):
    pass


if __name__ == '__main__':
    MainApp().run()
