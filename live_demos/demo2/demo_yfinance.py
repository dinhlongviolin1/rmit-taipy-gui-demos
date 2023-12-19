import yfinance as yf
from taipy.gui import Gui


stock_list = ["AAPL", "MSFT", "GOOG", "AMZN"]
stock_name = stock_list[0]
df = yf.Ticker(stock_name).history(interval="1d", period="1Y")
df["Date"] = df.index


def on_change(state, var, val):
    print(var, val)
    if var == "stock_name":
        state.df = yf.Ticker(val).history(interval="1d", period="1Y")
        state.df["Date"] = state.df.index


gui = Gui(
    page="""
# Stock price by day (1 years)

Stock Name: <|{stock_name}|selector|lov={stock_list}|>

<|{df}|chart|x=Date|y=Open|decimator=decimator_instance|>
"""
)
gui.run()
