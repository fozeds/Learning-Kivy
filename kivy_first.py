import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require("2.3.0")  # use isso para explicitar a mínima versão para rodar o app

class AppTeste(App):

    def build(self):   # esse método é chamado ao dar run no app
        return Label(text="hello world")

if __name__ == "__main__":
    AppTeste().run()  # método da classe App importada e inserida como Pai.
