from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class CalcDesign(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try :
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"

class calc(App):
    def build(self):
        return CalcDesign()

if __name__ == '__main__':
    app = calc()
    app.run()

