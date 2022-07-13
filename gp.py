import pandas as pd
import plotiy.express as px

df = pd.read_csv("data.csv")

fig = px.scatter(df,    x="data",
                        y="cases",
                        color="country"
            )
fig.show()            