#  http://www.pygal.org/
# Requires pip install pygal


from random import randint
import json
import pygal
from pygal.maps.world import COUNTRIES  # pip install pygal_maps_world
from pygal.maps.world import World      # pip install pygal_maps_world
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS, LightenStyle as LS
import requests   # see bezpy_26_requests.py


class Die():
    """A class representing a single die."""
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)



def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If the country wasn't found, return None.
    return None


if __name__ == '__main__':
    die = Die()
    die_2 = Die()

    results = []
    for _ in range(50000):
        result = die.roll() + die_2.roll()
        results.append(result)

    # Analyze the results.
    frequencies = []
    for value in range(2, 13):
        frequency = results.count(value)
        frequencies.append(frequency)


    hist = pygal.Bar()
    hist.title = "Results of rolling 2 dice and Summing."
    hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"
    hist.add('Sum of Dice', frequencies)
    hist.render_to_file(r'myfiles\die_visual.svg')




    for country_code in sorted(COUNTRIES.keys()):
        print(country_code, COUNTRIES[country_code])

    wm = World()
    wm.title = 'North, Central, and South America'

    wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
    wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
    wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
                             'gy', 'pe', 'py', 'sr', 'uy', 've'])
    wm.render_to_file(r'myfiles\americas.svg')



    # Load the data into a list.
    filename = r'myfiles\population_data.json'
    with open(filename) as f:
        pop_data = json.load(f)

    # Build a dictionary of population data.
    cc_populations = {}
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                cc_populations[code] = population

    # Group the countries into 3 population levels.
    cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
    for cc, pop in cc_populations.items():
        if pop < 10000000:
            cc_pops_1[cc] = pop
        elif pop < 1000000000:
            cc_pops_2[cc] = pop
        else:
            cc_pops_3[cc] = pop

    # See how many countries are in each level.
    print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

    wm_style = RS('#336699', base_style=LCS)
    wm = World(style=wm_style)
    wm.title = 'World Population in 2010, by Country'
    wm.add('0-10m', cc_pops_1)
    wm.add('10m-1bn', cc_pops_2)
    wm.add('>1bn', cc_pops_3)
    wm.render_to_file(r'myfiles\world_population.svg')



    # Make an API call, and store the response.
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    print("Status code:", r.status_code)

    # Store API response in a variable.
    response_dict = r.json()
    print("Total repositories:", response_dict['total_count'])

    # Explore information about the repositories.
    repo_dicts = response_dict['items']

    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])

        # Get the project description, if one is available.
        description = repo_dict['description']
        if not description:
            description = "No description provided."

        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': description,
            'xlink': repo_dict['html_url'],
            }
        plot_dicts.append(plot_dict)

    # Make visualization.
    my_style = LS('#333366', base_style=LCS)
    my_style.title_font_size = 24
    my_style.label_font_size = 14
    my_style.major_label_font_size = 18

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.title = 'Most-Starred Python Projects on GitHub'
    chart.x_labels = names

    chart.add('', plot_dicts)
    chart.render_to_file('python_repos.svg')