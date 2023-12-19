import pandas as pd
import numpy as np
from taipy.gui import Gui
from taipy.gui.data.decimator import ScatterDecimator

from sklearn.datasets import make_classification

n_clusters = 3
n_features = 5

X, y = make_classification(
    n_samples=100000,
    n_features=n_features,
    n_informative=n_features,
    n_repeated=0,
    n_redundant=0,
    n_classes=n_clusters,
    class_sep=n_clusters,
)
df = pd.DataFrame(X[:, :3], columns=["x", "y", "z"])
df["class"] = y


def create_colors(y):
    colors = []
    for i in range(len(y)):
        if y[i] == 0:
            colors += ["red"]
        if y[i] == 1:
            colors += ["blue"]
        if y[i] == 2:
            colors += ["green"]
    return colors


# Print out number of points after decimation
def on_change(state, var, val):
    print(var, val)


df["Colors"] = create_colors(y)

marker = {"color": "Colors"}

# threshold: minimum number of points within data to apply decimator
# binning_ratio: the divider that determines the grid size. Basically, the larger the binning_ratio, the smaller the final chart points
# max_overlap_points: determines if how many points can overlap within a single grid area.

# decimator_instance = ScatterDecimator(threshold=100, binning_ratio=3, max_overlap_points=1)
decimator = ScatterDecimator(binning_ratio=30)

chart = """
<|layout|

<|{df}|chart|type=Scatter3D|x=x|y=y|z=z|marker={marker}|mode=markers|height=800px|decimator=decimator|>

<|{df}|chart|type=Scatter3D|x=x|y=y|z=z|marker={marker}|mode=markers|height=800px|>

|>
"""


Gui(page=chart).run()
