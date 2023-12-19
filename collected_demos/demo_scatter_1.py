from sklearn.datasets import make_blobs
import pandas as pd
from taipy.gui import Gui
from taipy.gui.data.decimator import ScatterDecimator, RDP

features, clusters = make_blobs(n_samples=10000000, n_features=2, centers=3, cluster_std=1, shuffle=False)
df = pd.DataFrame(features, columns=["A","B"])

# threshold: minimum number of points within data to apply decimator
# binning_ratio: the divider that determines the grid size. Basically, the larger the binning_ratio, the smaller the final chart points
# max_overlap_points: determines if how many points can overlap within a single grid area.
decimator_instance = ScatterDecimator(threshold=100, binning_ratio=3, max_overlap_points=1)

# Get the decimation point count
def on_change(state, var, val, module):
    print(var, val, module)

gui = Gui(page="""
<|{df}|chart|mode=markers|x=A|y=B|decimator=decimator_instance|height=500px|>
""")
gui.run(run_browser=False)