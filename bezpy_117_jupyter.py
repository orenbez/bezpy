# ===============================================================================================================
# Module ipython  (requires 'pip install ipython') provides interactive shell
# The shell is enumerated, starting with  ...
# In [1]:
# It supports system commands, like: ls or cat the tab key will show hints, which makes the session with
# interactive programming much more pleasant. You can also use up/down arrows to search for recent commands
# Module 'jupyter' builds on ipython as a prerequisite and requires `pip install jupyter`
# Full Excellent Jupyter Notebooks Tutorial: https://youtu.be/HW29067qVWk
# ===============================================================================================================

# ===============================================================================================================
# START:
# ===============================================================================================================
# activate virtual environment where jupyter is installed
# enter in windows command prompt `jupyter notebook` which runs a local server that you need to keep running
# 'http://localhost:8888/tree' opens up in your browser
# jupyter files are saved as .ipynb which is basically a json file
# File -> Download as HTML/PDF

# ===============================================================================================================
# HOW TO USE: 
# ===============================================================================================================
# File -> New Notebook  (creates untitled notebook Untitled.ipynb which you can rename)
# File -> Rename (to rename the notebook, or just click in 'untitled'
# Cell -> Cell Type -> Markdown (to set cell as a markdown cell)

# you can be in command mode (press ESC to got to command mode) or edit mode (press ENTER to go to edit mode)
# BASH COMMANDS: start cell with '!' to enter a bash command e.g. !pip list
# LINE MAGIC: start cell line with '%' for a line magic command
# CELL MAGIC: start cell with '%%' for a cell magic command

# enter '%lsmagic' in cell to list all the line magic commands and cell magic commands
# enter '%pwd' for cell to print current working directory (this is a line magic command)
# enter '%matplotlib inline' to allow matplot lib charts on a cell further down
# enter '%%HTML' to enable html contentent in that cell (this is a cell magic command)
# enter '%%timeit' to time execution of that cell (performed 100,000 times)
# you can display pandas datframes in a cell

# see  ./notebooks/oren_notebook.ipynb
# see  ./notebooks/digraph.ipynb  (uses graphviz module to display graphs)
# search google for jupyter galleries to see more examples