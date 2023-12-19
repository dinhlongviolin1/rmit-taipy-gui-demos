# Using markdown
from taipy import Gui

x = 30
y = 20
s = "Hello World"


def on_change(state, var, val):
    print(f"on_change: {var} = {val}")

def on_click(state):
    state.s = f"{state.s}!"


md = """
# Hello World

This is a demo of Taipy GUI.

## Variables

x = <|{x}|>

Slider for x (0 - 100): <|{x}|slider|>

y = <|{y}|>

Input for y: <|{y}|number|>

x + y = <|{x + y}|>

<|x - y = {x - y}|>

## Buttons

s = <|{s}|>

<|Update text for s|button|on_action=on_click|>

"""

Gui(page=md).run()
