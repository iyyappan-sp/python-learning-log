def on_button_click(callback):
    print("✅ Button Clicked")
    callback()

def show_message():
    print("✋ Hello Iyyappan, Welcome")

on_button_click(show_message)
