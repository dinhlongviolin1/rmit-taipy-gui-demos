import pandas as pd
import numpy as np
from taipy.gui import Gui
from taipy.gui.data.decimator import MinMaxDecimator, RDP, LTTB

df = pd.DataFrame(np.random.randint(0, 10000000, size=(300000, 1)), columns=["A"])
df["index1"] = df.index

# Use one of these for testing

# Based on epsilon
# decimator_instance = RDP(epsilon=100)

# Based on desired number of points
# decimator_instance = RDP(n_out=1000)

# decimator_instance = LTTB(n_out=300)

# decimator_instance = MinMaxDecimator(n_out=500)

gui = Gui(
    page=""" 
<|{df}|chart|x=index1|y=A|decimator=decimator_instance|>
"""
)
gui.run(run_browser=False)
