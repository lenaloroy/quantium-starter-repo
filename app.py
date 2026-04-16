import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "formatted_output.csv"

df = pd.read_csv(DATA_PATH)
df["Date"] = pd.to_datetime(df["Date"])

daily = df.groupby("Date", as_index=False)["Sales"].sum().sort_values("Date")

cutoff = pd.Timestamp("2021-01-15")

fig = px.line(daily, x="Date", y="Sales")
fig.update_xaxes(title_text="Date")
fig.update_yaxes(title_text="Sales")
fig.add_vline(x=cutoff, line_dash="dash", line_color="red")

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1("Pink Morsel Sales Before vs After 15 Jan 2021"),
        dcc.Graph(figure=fig),
    ]
)


if __name__ == "__main__":
    app.run(debug=True)