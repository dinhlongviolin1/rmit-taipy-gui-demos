import yfinance as yf
from taipy.gui import Gui
from taipy.gui.data.decimator import MinMaxDecimator, RDP, LTTB


df_AAPL = yf.Ticker("AAPL").history(interval="1d", period = "100Y")
df_AAPL["DATE"] = df_AAPL.index.astype(int).astype(float)


# decimator_instance = RDP(epsilon=1, threshold=10)
# decimator_instance = RDP(n_out=1000)
# decimator_instance = LTTB(n_out=300)
decimator_instance = MinMaxDecimator(n_out=500)

decimate_data_count = len(df_AAPL)

def on_change(state, var, val):
    if str(var).endswith("nb_rows"):
        state.decimate_data_count = val


gui = Gui(
    page="""
<|Data count original: {len(df_AAPL)}|>

<|Data count after decimation: {decimate_data_count}|>

<|{df_AAPL}|chart|x=DATE|y=Open|decimator=decimator_instance|>

<|{df_AAPL}|chart|x=DATE|y=Open|>

"""
)
gui.run()
