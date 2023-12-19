import taipy.gui.builder as tp
from taipy.gui import Gui

input_name = ""
name = ""

# This function will be executed when a variable changes on the frontend side
def on_change(state):
    if state.input_name == "":
        state.name = ""
        return
    state.name = f"Hello {state.input_name}!"

with tp.Page() as page:
    tp.input("{input_name}", label="Name")
    tp.input("{name}", label="Greeting!")

Gui(page=page).run(run_browser=False)