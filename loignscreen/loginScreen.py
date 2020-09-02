from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.animation import Animation

Window.size = (300, 500)


class LoginScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(LoginScreen(name="login"))


class loginscreenApp(MDApp):
    def build(self):
        return


app = loginscreenApp()
app.run()
