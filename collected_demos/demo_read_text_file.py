from taipy.gui import Gui

file_path = ""
text = ""

def on_change(state, var, val):
    if var == "file_path":
        file_content = open(val, "r").read()
        state.text = file_content

md = """
# File Viewer
File Selector: <|{file_path}|file_selector|label=Upload a file|extensions=".txt"|>

<|{text}|>
"""
gui = Gui(page=md)
gui.run()