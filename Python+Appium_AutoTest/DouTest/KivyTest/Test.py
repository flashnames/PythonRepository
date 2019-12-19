from kivy.app import App
from kivy.uix.label import Label


class TestApp(App):
    def Build(self):
        return Label(text='hello world')


if __name__=="__main__":
    TestApp().run()
