import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
df = pd.read_csv("C:/Users/pankaj/Desktop/coding/c97/py/data2.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Average Rating"], show_hist=True)
fig.show()
