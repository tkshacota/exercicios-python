from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField

KV = '''
<CalculatorApp>:
    orientation: 'vertical'
    padding: dp(20)
    spacing: dp(10)

    MDTextField:
        id: input_field
        hint_text: "0"
        helper_text_mode: "on_focus"
        font_size: "32sp"
        halign: "right"
        readonly: True

    GridLayout:
        cols: 4
        spacing: dp(10)
        size_hint_y: 0.8

        MDRaisedButton:
            text: "1"
            on_press: app.on_number_press(1)
        MDRaisedButton:
            text: "2"
            on_press: app.on_number_press(2)
        MDRaisedButton:
            text: "3"
            on_press: app.on_number_press(3)
        MDRaisedButton:
            text: "+"
            on_press: app.on_operator_press("+")

        MDRaisedButton:
            text: "4"
            on_press: app.on_number_press(4)
        MDRaisedButton:
            text: "5"
            on_press: app.on_number_press(5)
        MDRaisedButton:
            text: "6"
            on_press: app.on_number_press(6)
        MDRaisedButton:
            text: "-"
            on_press: app.on_operator_press("-")

        MDRaisedButton:
            text: "7"
            on_press: app.on_number_press(7)
        MDRaisedButton:
            text: "8"
            on_press: app.on_number_press(8)
        MDRaisedButton:
            text: "9"
            on_press: app.on_number_press(9)
        MDRaisedButton:
            text: "*"
            on_press: app.on_operator_press("*")

        MDRaisedButton:
            text: "C"
            on_press: app.clear_input()
        MDRaisedButton:
            text: "0"
            on_press: app.on_number_press(0)
        MDRaisedButton:
            text: "="
            on_press: app.calculate_result()
        MDRaisedButton:
            text: "/"
            on_press: app.on_operator_press("/")
'''


class CalculatorApp(BoxLayout):
    def on_number_press(self, number):
        current_text = self.ids.input_field.text
        if current_text == "Erro":
            current_text = ""
        self.ids.input_field.text = f"{current_text}{number}"

    def on_operator_press(self, operator):
        current_text = self.ids.input_field.text
        if current_text and current_text != "Erro":
            self.ids.input_field.text = f"{current_text} {operator} "

    def clear_input(self):
        self.ids.input_field.text = ""

    def calculate_result(self):
        try:
            expression = self.ids.input_field.text
            if expression:
                result = eval(expression)
                self.ids.input_field.text = str(result)
        except Exception:
            self.ids.input_field.text = "Erro"


class CalculatorMDApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return CalculatorApp()

    def on_number_press(self, number):
        self.root.on_number_press(number)

    def on_operator_press(self, operator):
        self.root.on_operator_press(operator)

    def clear_input(self):
        self.root.clear_input()

    def calculate_result(self):
        self.root.calculate_result()


if __name__ == '__main__':
    Builder.load_string(KV)
    CalculatorMDApp().run()