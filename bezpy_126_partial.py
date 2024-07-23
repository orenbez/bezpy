# allows the partial application of a function. 
# Suppose there is a function with lots of arguments but you need to change 
# only one or two argument every time you use that function, 
# Partial function comes to the rescue
# can be used to clone functions while preserving some of their arguments with custom values


from functools import partial

import pandas as pd

partial_read_csv = partial(pd.read_csv, delimiter="|", index_col="date", true_values="true")


partial_read_csv("data/specially_formatted.csv") # the other argument values are already set