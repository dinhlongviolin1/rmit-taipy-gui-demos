from taipy.gui import Gui
import taipy.gui.builder as tp
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text = ""
result = {"name": [], "value": []}

nltk.download("vader_lexicon")
sid = SentimentIntensityAnalyzer()

def analyze(state):
    scores = sid.polarity_scores(state.text)
    del scores["compound"]
    state.result = {
        "name": scores.keys(),
        "value": scores.values()         
    }

with tp.Page() as page:
    tp.input("{text}", label="Input Text")
    tp.button("Analyze", on_action="analyze")
    tp.text("Sentiment Analysis Result")
    tp.table("{result}")

Gui(page=page).run(run_browser=False)