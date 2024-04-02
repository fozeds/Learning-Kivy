from random import randint, random

from kivy.app import App
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        # print(touch)  # printa a posição (pos) em relação a tela e posição (spos) em relação ao widget
        with self.canvas:
            # Color(1, 1, 0)  # cor rgb amarela
            Color(random(), random(), random())
            d = 5.  # tamanho
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))  # cria uma ellipse com o tamanho d
            touch.ud['line'] = Line(points=(touch.x, touch.y))  # cria uma linha
            touch.ud["wtf"] = Line(points=(touch.x, touch.y)) #ud é um dicionário onde vc pode adicionar novas propriedades ao touch.

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y] # na lista do objeto line inserinda no dicionário ud do touch, está sendo colocada uma lista de pontos
        touch.ud['wtf'].points += [touch.x + randint(1, 5), touch.y - randint(1, 5)]
        # print(touch.x, touch.y)
        # print(touch.ud['line'].points)

class MyPaintApp(App):
    def build(self):
        parent = Widget()  # definindo um widget pai
        self.painter = MyPaintWidget()  # instanciando o widget mypaint.
        clearbtn = Button(text='Clear')  # definindo um botão clear.
        clearbtn.bind(on_release=self.clear_canvas)  # atribuindo a função do botão ao soltar, que é executar self.clear_canvas
        parent.add_widget(self.painter)  # adicionando o widget mypaint no widget pai (janela principal)
        parent.add_widget(clearbtn)  # adicionando o widget do objeto clearbtn no widget pai.
        return parent

    def clear_canvas(self, obj):  # não sei pq diabos o bind envia ele mesmo como objeto.
        print(obj)
        self.painter.canvas.clear()    # limpa os elementos feitos em canvas


if __name__ == '__main__':
    MyPaintApp().run()
