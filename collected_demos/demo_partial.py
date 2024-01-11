import random
from taipy.gui import Gui

# Random layout declaration in markdown
layout_list = [
"""
a = <|{a}|>

a + 10 = <|{a + 10}|>

<|Change Layout|button|on_action=change_layout|>
""",

"""
<|Change Layout|button|on_action=change_layout|>

a = <|{a}|>

a + 10 = <|{a + 10}|>
""",

"""
a = <|{a}|>

<|Change Layout|button|on_action=change_layout|>

a + 10 = <|{a + 10}|>
""",
]

# variable declaration
a = 10
current_layout_no = 0

# Gui initialization with a simple page only using partial
gui = Gui(
    page="""
# Layout <|{current_layout_no + 1}|raw=True|>

<|part|partial={main_partial}|>
"""
)

# create a partial
main_partial = gui.add_partial(layout_list[current_layout_no])


# Handle button press to change to a different layout
def change_layout(state):
    # Get a random layout different for the current one
    state.current_layout_no = random.choice(
        list(range(state.current_layout_no))
        + list(range(state.current_layout_no + 1, len(layout_list)))
    )
    main_partial.update_content(state, layout_list[state.current_layout_no])


gui.run()
