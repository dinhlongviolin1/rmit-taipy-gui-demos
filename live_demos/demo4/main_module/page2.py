from taipy.gui import Markdown

def reset_to_10(state):
    state.x = 10
    state.y = 10

md = """
# Page 2
x = <|{x}|>

Slider for x: <|{x}|slider|>

y = <|{y}|>

Slider for y: <|{y}|slider|>

x + y = <|{x + y}|>

<|Reset to 10|button|on_action=reset_to_10|>
"""
page = Markdown(md)
