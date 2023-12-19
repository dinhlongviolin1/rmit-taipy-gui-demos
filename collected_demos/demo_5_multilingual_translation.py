from taipy.gui import Gui
import taipy.gui.builder as tp
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch

model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")
device = 0 if torch.cuda.is_available() else -1
LANGS = ["ace_Arab", "eng_Latn", "fra_Latn", "spa_Latn"]

def translate(state):
    translation_pipeline = pipeline("translation", model=model, tokenizer=tokenizer, src_lang=state.src_lang, tgt_lang=state.tgt_lang, max_length=400, device=device)
    result = translation_pipeline(state.inp)
    state.out = result[0]['translation_text']

inp = ""
src_lang = ""
tgt_lang = ""
out = ""

with tp.Page() as page:
    tp.input("{inp}", label="Input Text")
    tp.selector("{src_lang}", label="Source Language", lov="{LANGS}")
    tp.selector("{tgt_lang}", label="Target Language", lov="{LANGS}")
    tp.button("Translate", on_action="translate")
    tp.input("{out}", label="Output Text")

Gui(page=page).run(run_browser=False)