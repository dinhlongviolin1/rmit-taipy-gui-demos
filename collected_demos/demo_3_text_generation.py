from taipy.gui import Gui
import taipy.gui.builder as tp
from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')

text = ""
result = ""

def generate(state):
    result = generator(state.text, max_length=30, num_return_sequences=1)
    state.result = result[0]["generated_text"]


with tp.layout() as main_layout:
    with tp.part():
        tp.input("{text}", label="Input Text", multiline="True")
        tp.button("Generate Text", on_action="generate")
    tp.input("{result}", label="Generated Text", multiline="True")

Gui(page=tp.Page(main_layout)).run(run_browser=False)
