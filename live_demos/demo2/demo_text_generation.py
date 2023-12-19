from taipy.gui import Gui
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

text = ""
result = ""


def generate(state):
    result = generator(state.text, max_length=30, num_return_sequences=1)
    state.result = result[0]["generated_text"]


md = """
# Text Generation Demo

<|{text}|input|label=Input Text|>

<|Generate Text|button|on_action=generate|>

<|{result}|input|label=Generated Text|multiline=True|>

"""

Gui(page=md).run(run_browser=False)
