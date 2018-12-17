import numpy as np

import plotly
import plotly.graph_objs as go
from plotly import tools


x10 = np.linspace(-2*np.pi, 2*np.pi,10)
x50 = np.linspace(-2*np.pi, 2*np.pi,50)
x100 = np.linspace(-2*np.pi, 2*np.pi,100)

cos10 = np.cos(x10)
cos50 = np.cos(x50)
cos100 = np.cos(x100)

sin100 = np.sin(x100)


sin_trace = go.Scatter(x=x100,y=sin100, name="sin")

cos_trace10 = go.Scatter(x=x10,y=cos10, name="cos10")
cos_trace50 = go.Scatter(x=x50,y=cos50, name="cos50")
cos_trace100 = go.Scatter(x=x100,y=cos100, name="cos100")

inverse_x = go.Scatter(x=x100,y=1/x100, name="1/x")

bar = go.Bar(
    x=["apple","lemon","cake"],
    y=[10,14,17],
    name="Bar"
)



fig = tools.make_subplots(rows=2, cols=2)

fig.append_trace(sin_trace, 1, 1)

fig.append_trace(cos_trace10, 1, 2)
fig.append_trace(cos_trace50, 1, 2)
fig.append_trace(cos_trace100, 1, 2)

fig.append_trace(bar, 2, 1)
fig.append_trace(inverse_x, 2, 2)


plotly.offline.plot(fig, filename='plotly.html')




