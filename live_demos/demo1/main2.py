# Using markdown with a separate file
from taipy.gui import Gui, Markdown

x = 30
y = 20
s = "Hello World"


def on_change(state, var, val):
    print(f"on_change: {var} = {val}")


def on_click(state):
    state.s = f"{state.s}!"


Gui(page=Markdown("main2.md")).run()
