# Get this figure: fig = py.get_figure("https://plot.ly/~KyleMcLean/1/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~KyleMcLean/1/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="Plot 1", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~KyleMcLean/1/").get_data()[0]["y"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api
import plotly
import plotly
plotly.tools.set_credentials_file(username='KyleMcLean', api_key='QcfZoiRY2nkWnEYRTJgB')

import plotly.plotly as py
from plotly.graph_objs import *

py.sign_in('KyleMcLean', 'cfZoiRY2nkWnEYRTJgB')
trace1 = {
  "x": ["Average Price", "1723", "1054.5", "1730.167", "1227.778", "1350", "2800", "1701.933", "1322.5", "1100", "949.5", "960", "1149", "864", "850", "1149", "1475.875", "1500", "1552.091", "1750", "4000", "1411.5", "3400", "1425.826", "1004.667", "1347", "1425", "1582.995", "1200", "1500", "2749.5", "1049.133", "1008.944", "2000", "1200", "1072.824", "2000", "920.9667", "1595", "1838.5", "1322.143", "700", "943.2069", "2200.6", "1650", "1895", "1250", "1950", "1481.667", "1475", "1600", "1217.125", "2242.5", "1029", "1508", "1010", "1831.7", "1645", "2276.75", "1500", "1508.871", "1207.25", "991.2"],
  "y": ["Total Listings", "", "21", "6", "9", "4", "1", "14", "2", "1", "4", "1", "2", "1", "2", "2", "15", "2", "21", "3", "1", "4", "1", "22", "3", "4", "2", "21", "1", "1", "2", "14", "17", "1", "1", "16", "1", "30", "1", "6", "13", "1", "28", "5", "1", "1", "1", "3", "3", "1", "1", "8", "2", "6", "7", "4", "10", "1", "4", "1", "41", "12", "5"],
  "z": ["SD", "", "329.15", "1018.427", "134.9099", "334.1656", "0", "764.0909", "53.03301", "0", "289.2525", "0", "70.71068", "0", "0", "0", "271.6154", "0", "456.1745", "433.0127", "0", "131.4978", "0", "323.3457", "82.94777", "326.4769", "318.1981", "308.671", "0", "0", "70.00357", "203.3757", "279.5573", "0", "0", "205.2463", "0", "134.885", "0", "711", "127.6521", "0", "334.6217", "988.5921", "0", "0", "0", "50", "54.84828", "0", "0", "226.6691", "915.7033", "57.77226", "355.9476", "20", "845.5922", "0", "260.4616", "0", "515.6106", "164.3246", "134.2542"],
  "mode": "markers",
  "name": "Column 5",
  "text": ["location", "12th South", "Antioch", "Belle Meade", "Bellevue", "Bellmont-Hillsboro", "Breeze Hill", "Brentwood", "Centennial Park", "Charlotte Park", "Clarksville", "Colmbia", "Cool Springs", "Croley Wood", "Cumberland Gardens", "Donelson", "Downtown", "East End", "East Nashville", "Edgefield", "Edgehill", "Elliston", "Fair Grounds", "Franklin", "Gallatin", "Germantown", "Glencliff", "Green Hills", "Hadley Park", "Hargis Heights", "Haynes Area", "HendersonVille", "Hermitage", "Hillwood", "LaVerge", "Lebanon", "Lockland Springs", "Madison", "Marrowbone", "Melrose", "Mt Juliet", "Mt Pleasant", "Murfeesboro", "Music Row", "Pie Town", "Quailtrail", "Radnor", "Raintrec", "River Glen", "Rose Bank", "Shelbyville", "Smyrna", "SoBro", "Southeast Nashville", "Spring Hill", "Springfield", "Sylvan Park", "Talbot's Corner", "The Gultch", "Wedgewood", "West End", "West Nashville", "White Bridge"],
  "textsrc": "KyleMcLean:0:89cb85",
  "type": "scatter3d",
  "uid": "6c8c88",
  "xsrc": "KyleMcLean:0:b45b94",
  "ysrc": "KyleMcLean:0:f3cba0",
  "zsrc": "KyleMcLean:0:9b150c"
}
data = Data([trace1])
layout = {
  "autosize": True,
  "boxmode": "group",
  "hovermode": "closest",
  "scene": {
    "aspectratio": {
      "x": 1,
      "y": 1,
      "z": 1
    },
    "camera": {
      "center": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "eye": {
        "x": 0.318928701808,
        "y": -1.81978317647,
        "z": 0.967264666566
      },
      "up": {
        "x": 0,
        "y": 0,
        "z": 1
      }
    }
  },
  "xaxis": {"title": "Column 3"},
  "yaxis": {"title": "Column 4"}
}
frame1 = {
  "data": [
    {"type": "scatter"}
  ],
  "group": "populate-transform-__animation_slider_id__",
  "name": "slider-__animation_slider_id__-1",
  "traces": [0]
}
frame2 = {
  "data": [
    {"type": "scatter"}
  ],
  "group": "populate-transform-__animation_slider_id__",
  "name": "slider-__animation_slider_id__-2",
  "traces": [0]
}
frame3 = {
  "data": [
    {"type": "scatter"}
  ],
  "group": "populate-transform-__animation_slider_id__",
  "name": "slider-__animation_slider_id__-3",
  "traces": [0]
}
frame4 = {
  "data": [
    {"type": "scatter"}
  ],
  "group": "populate-transform-__animation_slider_id__",
  "name": "slider-__animation_slider_id__-12",
  "traces": [0]
}
frame5 = {
  "data": [
    {"type": "scatter"}
  ],
  "group": "populate-transform-__animation_slider_id__",
  "name": "slider-__animation_slider_id__-13",
  "traces": [0]
}
frame6 = {
  "data": [
    {"type": "scatter"}
  ],
  "group": "populate-transform-__animation_slider_id__",
  "name": "slider-__animation_slider_id__-14",
  "traces": [0]
}
frame7 = {
  "data": [
    {"type": "scatter"}
  ],
  "group": "populate-transform-__animation_slider_id__",
  "name": "slider-__animation_slider_id__-15",
  "traces": [0]
}
frame8 = {
  "data": [
    {"type": "scatter"}
  ],
  "group": "populate-transform-__animation_slider_id__",
  "name": "slider-__animation_slider_id__-16",
  "traces": [0]
}
frame9 = {
  "data": [
    {"type": "scatter"}
  ],
  "group": "populate-transform-__animation_slider_id__",
  "name": "slider-__animation_slider_id__-17",
  "traces": [0]
}
frame10 = {
  "data": [
    {"type": "scatter"}
  ],
  "group": "populate-transform-__animation_slider_id__",
  "name": "slider-__animation_slider_id__-21",
  "traces": [0]
}
frame11 = {
  "data": [
    {"type": "scatter"}
  ],
  "group": "populate-transform-__animation_slider_id__",
  "name": "slider-__animation_slider_id__-22",
  "traces": [0]
}
frame12 = {
  "data": [
    {"type": "scatter"}
  ],
  "group": "populate-transform-__animation_slider_id__",
  "name": "slider-__animation_slider_id__-28",
  "traces": [0]
}
frame13 = {
  "data": [
    {"type": "scatter"}
  ],
  "group": "populate-transform-__animation_slider_id__",
  "name": "slider-__animation_slider_id__-30",
  "traces": [0]
}
frame14 = {
  "data": [
    {"type": "scatter"}
  ],
  "group": "populate-transform-__animation_slider_id__",
  "name": "slider-__animation_slider_id__-41",
  "traces": [0]
}
frame15 = {
  "data": [
    {"type": "scatter"}
  ],
  "group": "populate-transform-__animation_slider_id__",
  "name": "slider-__animation_slider_id__-Total Listings",
  "traces": [0]
}
frame16 = {
  "data": [
    {"type": "scatter"}
  ],
  "group": "populate-transform-__animation_slider_id__",
  "name": "slider-__animation_slider_id__-",
  "traces": [0]
}
frames = Frames([frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10, frame11, frame12, frame13, frame14, frame15, frame16])

# Frames are not yet supported for use with Python.
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
