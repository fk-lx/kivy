from common import GraphicUnitTest


class UIXWidgetTestCase(GraphicUnitTest):

    def test_default_widgets(self):
        from kivy.uix.button import Button
        from kivy.uix.slider import Slider
        r = self.render
        r(Button())
        r(Slider())

    def test_button_properties(self):
        from kivy.uix.button import Button
        r = self.render
        # test label attribute inside button
        r(Button(text='Hello world'))
        r(Button(text='Multiline\ntext\nbutton'))
        r(Button(text='Hello world', font_size=42))
        r(Button(text='This is my first line\nSecond line', halign='center'))

    def test_slider_propperties(self):
        from kivy.uix.slider import Slider
        r = self.render
        r(Slider(value=25), 2)
        r(Slider(value=50), 2)
        r(Slider(value=100), 2)
        r(Slider(min=-100, max=100, value=0), 2)

    '''
    def test_default_label(self):
        from kivy.uix.label import Label
        self.render(Label())

    def test_button_state_down(self):
        from kivy.uix.button import Button
        self.render(Button(state='down'))

    def test_label_text(self):
        from kivy.uix.label import Label
        self.render(Label(text='Hello world'))

    def test_label_font_size(self):
        from kivy.uix.label import Label
        self.render(Label(text='Hello world', font_size=16))

    def test_label_font_size(self):
        from kivy.uix.label import Label
        self.render(Label(text='Hello world'))
    '''