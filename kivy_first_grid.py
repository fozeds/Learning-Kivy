from kivy import require
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

require("2.3.0")

class LoginScreen(GridLayout):  # classe do grid

    def __init__(self, **kwargs):  # init do grid
        super(LoginScreen, self).__init__(**kwargs)  # sobrescrevendo  o construtor da class mãe
        self.cols = 2  # dizendo o numero de colunas que a grid tem
        self.username = TextInput(multiline=False)   # criando uma box de input_text username, impedindo multi linhas.
        self.password = TextInput(password=True, multiline=False)  # criando uma input_text password
        self.add_widget(Label(text='User Name'))  # adicionando um texto na posição (0, 0)
        self.add_widget(self.username)  # criando uma instancia de username e adicionando no layout
        self.add_widget(Label(text='password'))  # adicionando texto na posição (1,0)
        self.add_widget(self.password) # instancia de password na posição (1,1)


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()