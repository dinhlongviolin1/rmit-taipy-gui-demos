# Using Taipy GUI Builder
from taipy import Gui
import taipy.gui.builder as tgb

x = 30
y = 20
s = "Hello World"


def on_change(state, var, val):
    print(f"on_change: {var} = {val}")

def on_click(state):
    state.s = f"{state.s}!"

with tgb.Page() as page:
    tgb.html("h1", "Hello World")
    tgb.html("p", "This is a demo of Taipy GUI.")
    tgb.html("h2", "Variables")
    tgb.text("x = {x}")
    tgb.text("Slider for x (0 - 100):")
    tgb.slider("{x}")
    tgb.text("y = {y}")
    tgb.text("Input for y:")
    tgb.number("{y}")
    tgb.text("x + y = {x + y}")
    tgb.text("x - y = {x - y}")
    tgb.html("h2", "Buttons")
    tgb.text("s = {s}")
    tgb.button("Update text for s", on_action=on_click)

Gui(page=page).run()
