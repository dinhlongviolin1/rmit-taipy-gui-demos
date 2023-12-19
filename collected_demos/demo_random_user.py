from taipy.gui import Gui
import requests

url = "https://randomuser.me/api/?results=10"


def get_data():
    r = requests.get(url)
    data = r.json()["results"]
    d = {"gender": [], "name": []}
    for i in data:
        d["gender"].append(i["gender"])
        d["name"].append(i["name"]["first"])
    return d


data = get_data()


def refresh(state):
    state.data = get_data()


md = """
# Display random user data

<|Refresh data|button|on_action=refresh|>

<|{data}|table|>
"""

gui = Gui(page=md)
gui.run()
