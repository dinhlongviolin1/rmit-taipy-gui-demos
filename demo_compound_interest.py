from taipy.gui import Gui
import pandas as pd

# Initialize variables
interest_rate = 8
contribution_increase_rate = 10
saving_term = 5
deposit_amount = 0
monthly_contribution = 5000

# Setting up a variable that will be used for populating the chart
chart_data = pd.DataFrame(columns=["Year", "Contribution", "Interest", "Total"])


# This function will be executed when the user clicks the "Calculate" button
def calculate(state):
    calculate_data = []
    total_interest = 0
    total = state.deposit_amount
    contribution = state.monthly_contribution
    # Calculate compound interest
    for year in range(int(state.saving_term)):
        interest_rate_per_month = state.interest_rate / 100 / 12
        for _ in range(12):
            total = total * (interest_rate_per_month + 1) + contribution
            total_interest += total * interest_rate_per_month
        contribution = contribution * (state.contribution_increase_rate / 100 + 1)
        calculate_data.append((year + 1, total - total_interest, total_interest, total))
    # Update the chart through the state variable
    state.chart_data = pd.DataFrame(
        calculate_data, columns=["Year", "Contribution", "Interest", "Total"]
    )


page = """
# Compound interest rate calculator (compounded monthly)

<|layout|columns=6*1|

<|{deposit_amount}|number|label=Initial Deposit Amount (USD)|>

<|{monthly_contribution}|number|label=Monthly Contribution (USD)|>

<|{contribution_increase_rate}|number|label=Yearly Contribution Increase Rate (%)|>

<|{interest_rate}|number|label=Interest rate per year (%)|>

<|{saving_term}|number|label=Saving term (year)|>

<|Calculate|button|on_action=calculate|>

|>

<|{chart_data}|chart|type=bar|x=Year|y[1]=Interest|y[2]=Contribution|y[3]=Total|height=600px|>
"""

Gui(page=page).run()
