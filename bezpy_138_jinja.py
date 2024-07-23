# Jinja is a web template engine compared to smarty
# Requires `pip install jinja2`
# also used in pandas dataframe styling
# https://realpython.com/courses/jinja-templating/

# Example template mydata\example.html.jinja
# <!DOCTYPE html>
# <html>
#   <head>
#     <title>{{ variable|escape }}</title>
#   </head>
#   <body>
#   {%- for item in item_list %}
#     {{ item }}{% if not loop.last %},{% endif %}
#   {%- endfor %}
#   </body>
# </html>

from jinja2 import Template
with open('mydata\example.html.jinja') as f:
    tmpl = Template(f.read())

print(tmpl.render(variable = 'Value with <unsafe> data', item_list = [1, 2, 3, 4, 5, 6]))


# Generates:
# <!DOCTYPE html>
# <html>
#   <head>
#     <title>Value with &lt;unsafe&gt; data</title>
#   </head>
#   <body>
#     1,
#     2,
#     3,
#     4,
#     5,
#     6
#   </body>
# </html>