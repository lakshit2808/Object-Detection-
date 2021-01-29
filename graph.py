from main import df
from bokeh.plotting import figure , show , output_file
from datetime import datetime
from bokeh.models import HoverTool

fig = figure(x_axis_type='datetime', height = 100 , width = 500  , title = "Object Capture")
fig.yaxis.minor_tick_line_color=None

hover = HoverTool(tooltips=[("Start" , "@Start") , ("END" , "@END")])
fig.add_tools(hover)

plot = fig.quad(left=df["Start"] , right=df["END"] , bottom=0 ,top=1,color="green")

output_file("graph.html")

show(fig)

