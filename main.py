from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50)
        self.label = Label(text="مرحباً بك في تطبيقي الأول!", font_name="Arial")
        btn = Button(text="اضغط هنا", size_hint=(1, 0.5))
        btn.bind(on_press=self.on_button_press)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def on_button_press(self, instance):
        self.label.text = "لقد ضغطت على الزر! رائع."

if __name__ == '__main__':
    MyApp().run()
