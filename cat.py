import pandas as pd
import plotly.express as px
import csv

df = pd.read_csv("C:/Users/Administrator/Desktop/Python 2/projects/c107/data.csv")
mean = df.groupby(["studentid","level"])["attempt"].mean()
fig = px.scatter(mean,x="studentid",y="level",size = "attempt",color="attempt")
fig.show()