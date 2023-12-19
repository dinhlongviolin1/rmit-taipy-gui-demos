# Using html
from taipy.gui import Gui, Html

x = 30
y = 20
s = "Hello World"


def on_change(state, var, val):
    print(f"on_change: {var} = {val}")

def on_click(state):
    state.s = f"{state.s}!"

Gui(page=Html("main4.index.html")).run()
