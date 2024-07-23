# ==================================================================================================================================
# Plotting direct in pandas
# ==================================================================================================================================
# https://towardsdatascience.com/the-simplest-way-to-create-complex-visualizations-in-python-isnt-with-matplotlib-a5802f2dba92

# WARNING.  don't name file pandas.py
# import matplotlib.pyplot as plt   # IS NOT REQUIRED


import pandas as pd
import numpy as np
import seaborn as sns



# np.random.rand(x, y) generates random x * y array of numbers between 0 and 1
data = pd.DataFrame(np.random.rand(10, 4), columns=['A','B','C','D'])  # 10 ROWS 4 COLUMNS

data.plot()
data.plot.bar()             # Displays bar chart
data.plot.bar(stacked=True) # Will stack the columns A,B,C,D on the same value
sns.set_palette('magma')
data.plot.area()
data.plot.area(stacked=False)
data.diff().plot.box(vert=False, color={'medians':'lightblue', 'boxes':'blue','caps':'darkblue'});


data = pd.DataFrame(np.random.rand(100, 1), columns=['value']).reset_index()
data['value'].plot()
data['value'].hist(color = 'blue', edgecolor='black', bins=1400, grid=True)
data['value'].rolling(10).mean().plot()


data = pd.DataFrame(np.random.rand(10, 4), columns=['A','B','C','D'])  # 10 ROWS 4 COLUMNS
data.plot.kde(); #distribution plot  # i think this is the same as .plot(kind='kde')
data.plot.scatter(x='A',y='B', #scatterplot x and y
                  c='C',       #color of data points
                  s=data['C']*200); #size of data points

data.plot.hexbin(x='C',y='D', #hexbin x and y
                 gridsize=18); #hexagon dimensions



data = pd.DataFrame(np.random.rand(5, 2),
                    index=list("ABCDE"), 
                    columns=list("XY"))
data.plot.pie(subplots=True, figsize=(8, 4));


data = pd.DataFrame(np.random.rand(100, 4), columns=['A','B','C','D'])
data.plot(subplots=True,figsize=(20,10));


# requires pip install ipython
# requires pip install pandasgui

from pandasgui import show  # requires pip install IPython,  pip install pandasgui
from pandasgui.datasets import titanic, stockdata, penguins, pokemon, tips  # Sample Dataframes
gui = show(titanic)  # Opens a gui for the dataframe



# ======================================================================================================================
# Pandas styling  see notebooks/pandas_styling.ipynb for visual
# Requires `pip install jinja2`
# ======================================================================================================================
from IPython.display import display  # or use Jupyter and you don't need the display(df) method

df = pd.DataFrame({"A" : [14, 4, 5, 4, 1],
                   "B" : [5, 2, 54, 3, 2],
                   "C" : [20, 20, 7, 3, 8],
                   "D" : [14, 3, 6, 2, 6]})

def highlight_cols(s):
    color = 'red' if s < 6 else 'blue'
    return (f'background-color: {color}')

def highlight_cols2(s):
    return (f'background-color: yellow')

# highlights all elements either red or blue
display(df.style.applymap(highlight_cols))

# highlights Columns 'B' & 'C' yellow
display(df.style.applymap(highlight_cols, subset=pd.IndexSlice[:, ['B', 'C']]))

styler = df.style.applymap(highlight_cols)    # styler object
type(styler)  # pandas.io.formats.style.Styler
print(styler.to_html())    # renders html with css styling  - note that styler.render() is equivalent but deprecated as of pandas 1.4.0
print(df.to_html())        # renders html without css styling
df.style # returns style object


# from https://coderzcolumn.com/tutorials/python/simple-guide-to-style-display-of-pandas-dataframes
# also you should read: https://www.analyticsvidhya.com/blog/2021/06/style-your-pandas-dataframe-and-make-it-stunning/
data = np.random.random(size=(10,5))

df = pd.DataFrame(data=data, columns=list("ABCDE"),
                  index=["A1", "B2", "C3", "D4", "E5", "F6", "G7", "H8", "I9", "J10"])


# sets style for thead - the title row
s = df.style.set_table_styles([{"selector":"thead",
                                "props":"background-color:dodgerblue; color:white; border:3px solid red;"},])

# same as above
s = df.style.set_table_styles([{"selector":"thead",
                                "props": [("background-color", "dodgerblue"),
                                          ("color", "white"),
                                          ("border", "3px solid red"),]},])
# sets style for title row and index column
df.style.set_table_styles([{"selector":"thead",
                            "props": [("background-color", "dodgerblue"),
                                      ("color", "white"),
                                      ("border", "3px solid red"),
                                      ("font-size", "2rem"), ("font-style", "italic")]},
                            {"selector":"th.row_heading",
                             "props": [("background-color", "orange"), ("color", "green"),
                                          ("border", "3px solid black"),
                                          ("font-size", "2rem"), ("font-style", "italic")]},])

# sets style of column 'C'
df.style.set_table_styles({"C" : [{"selector" :"td",
                                   "props": [("border","2px solid red"),
                                             ("color", "green"),
                                             ("background-color", "yellow")]}]})
# sets style for an individual row
df.style.set_table_styles([{"selector" :".row1",
                            "props": [("border","2px solid red"),
                                      ("color", "green"),
                                      ("background-color", "yellow")]}])

# same as above
df.style.set_table_styles({"B2" : [{"selector" :"td",
                                     "props": [("border","2px solid red"),
                                               ("color", "green"),
                                               ("background-color", "yellow")]}]}, axis=1)

# individual cell
df.style.set_table_styles([{"selector" :".row1.col1",
                            "props": [("border","2px solid red"),
                                                  ("color", "green"),
                                                  ("background-color", "yellow")]}])

df.style.applymap(lambda x: "background-color:lime; font-size:1.5rem;" if x > 0.5 else "background-color:tomato; font-size:0.9rem;",
                      subset=["B", "D"])