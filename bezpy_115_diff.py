# requires `pip install deepdiff``
# Documentation: https://zepworks.com/deepdiff/current/
# https://towardsdatascience.com/deepdiff-recursively-find-and-ignore-trivial-differences-using-python-231a5524f41d


import pandas as pd
import numpy as np
from datetime import datetime as dt
from deepdiff import DeepDiff           # For Deep Difference of 2 objects
from deepdiff import grep, DeepSearch   # For finding if item exists in an object
from deepdiff import DeepHash           # For hashing objects based on their contents
from deepdiff import Delta              # For creating delta of objects that can be applied later to other objects.
from deepdiff import extract            # For extracting a path from an object


price1 = {'apple': 2, 'orange': 3, 'banana': [3, 2, 2]}
price2 = {'apple': 2, 'orange': 3, 'banana': [3, 2]}

# default is view='text'
DeepDiff(price1, price2)  # {'iterable_item_removed': {"root['banana'][2]": 2}}

DeepDiff(price1, price2, view='tree')  # {'iterable_item_removed': [<root['banana'][2] t1:2, t2:not present>]}

DeepDiff(price1, price2, ignore_order=True)  # {}

# Ignore significant_digits (decimal places) after 2
DeepDiff(1.344, 1.345, significant_digits=2)  # {}

# Ignore the difference that is smaller than 0.001
DeepDiff(0.344, 0.345, math_epsilon=0.001) # {'values_changed': {'root': {'new_value': 0.345, 'old_value': 0.344}}}

DeepDiff(0.999, 0.998, math_epsilon=0.01)  # {}

# Ignore Case differences
DeepDiff(['Dave', 'Fred'], ['dave', 'fred'], ignore_string_case=True)  # {}


# Ignore different types of NaNs  (does not equate to pd.NaT, pd.NA, or None)
x = [np.nan, float('nan')]
y = [float('nan'), np.nan]
DeepDiff(x, y, ignore_nan_inequality=True)  # {}

# Ignore numeric type
DeepDiff(2, 2.0, ignore_numeric_type_changes=True )   # {}

# Exclude Types
d1 = {'name': 'Fred', 'age': 7}
d2 = {'name': 'Dave', 'age': 7}
DeepDiff(d1, d2, exclude_types = [str])  # {}

# Truncate Datetime to ignore second differences and smaller
DeepDiff(dt(1974, 2, 20, 16, 10, 45), dt(1974, 2, 20, 16, 10, 44), truncate_datetime='second')  # {}

# Exclude Paths
d1 = {'name': 'Fred', 'age': 7, 'address': {'num': 5, 'street': 'Colindeep'}, 'height': 124}
d2 = {'name': 'Fred', 'age': 7, 'address': {'num': 5, 'street': 'Franklin'}, 'height': 123}
DeepDiff(d1, d2)  # {'values_changed': {"root['address']['street']": {'new_value': 'Franklin', 'old_value': 'Colindeep'}, "root['height']": {'new_value': 123, 'old_value': 124}}}
DeepDiff(d1, d2, exclude_paths={"root['address']['street']", "root['height']"})  # {}

# Exclude Regex Path
l1 = [{'price': 2, 'color': 'red'}, {'price': 2, 'color': 'red'}]
l2 = [{'price': 2, 'color': 'red'}, {'price': 2, 'color': 'green'}]
DeepDiff(l1, l2)  # {'values_changed': {"root[1]['color']": {'new_value': 'green', 'old_value': 'red'}}}
DeepDiff(l1, l2, exclude_regex_paths={r"root\[\d\]\['color'\]"}) # {}

# For PyTest can use 'assert not Deepdiff(...)' which is like 'assert not {}' if the DeepDiff is empty
assert not DeepDiff(0.999, 0.998, math_epsilon=0.01)
assert DeepDiff(0.999, 0.998, math_epsilon=0.01) == {}



# ===================================================
# Also note built-in library difflib
# This module provides facilities for computing differences between two sequences.
from difflib
line1 = "abcd"
line2 = "aecd"
list(difflib.Differ().compare(line1, line2))  # ['  a', '- b', '+ e', '  c', '  d']

# The dashes or minus signs indicate that “line2” doesn’t have these characters.
# Characters without any signs or leading whitespace are common to both variables.
# Characters with plus sign are available in the “line2” string only.

def compare__files(repo1_file, repo2_file):

    with open(repo1_file, encoding="utf-8") as file1,  open(repo2_file, encoding="utf-8") as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()

        #compare files
        differences = difflib.unified_diff(lines1, lines2, lineterm='')

        if differences is None:
            print("No differences found.")
            return None, None

        #Initialize lists to store diff
        added_lines = []
        removed_lines = []

        for line in differences:
            if line.startswith('+'):
                if line.strip('+').strip() != "":
                    added_lines.append(line.strip('+').strip())
            elif line.startswith('-'):
                if line.strip('-').strip() != "":
                    removed_lines.append(line.strip('-').strip())

        #create Dataframes
        added_df = pd.DataFrame(added_lines, columns=['Added Lines'])
        removed_df = pd.DataFrame(removed_lines, columns=['Removed Lines'])

        return added_df, removed_df