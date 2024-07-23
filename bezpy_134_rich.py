# python -m rich     --will display functinality of the rich module
# https://www.freecodecamp.org/news/use-the-rich-library-in-python/

from rich import print as rprint          # requires pip install rich

nums_list = [1, 2, 3, 4]
rprint(nums_list)

nums_tuple = (1, 2, 3, 4)
rprint(nums_tuple)

nums_dict = {'nums_list': nums_list, 'nums_tuple': nums_tuple}
rprint(nums_dict)

bool_list = [True, False]
rprint(bool_list)    # will display nicely from command line


from rich.console import Console
console = Console()

def merge_dict(dict_one, dict_two):
    merged_dict = dict_one | dict_two
    console.log(merged_dict, log_locals=True)

merge_dict({'id': 1}, {'name': 'Ashutosh'})


from rich.tree import Tree

tree = Tree("Family Tree")
tree.add("Mom")
tree.add("Dad")
tree.add("Brother").add("Wife")
tree.add("[red]Sister").add("[green]Husband").add("[blue]Son")

rprint(tree)