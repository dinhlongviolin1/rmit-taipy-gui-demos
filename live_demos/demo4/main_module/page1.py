from taipy.gui import Markdown

x = 50

def reset_to_0(state):
    state.x = 0
    state.y = 0

md = """
# Page 1
x = <|{x}|>

Slider for x: <|{x}|slider|>

y = <|{y}|>

Slider for y: <|{y}|slider|>

x + y = <|{x + y}|>

<|Reset to 0|button|on_action=reset_to_0|>
"""
page = Markdown(md)
