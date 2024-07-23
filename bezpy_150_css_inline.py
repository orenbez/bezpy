# css_inline-0.13.0: converts internal to inline css
# other pypi alternatives: premailer, toronado, inlinestyler, pynliner are not active packages
# https://pypi.org/project/css-inline/


import css_inline
# INTERNAL CSS
# <html>
#   <head>
#     <style>h1 { color:blue; }</style>
#   </head>
#   <body>
#     <h1>Big Text</h1>
#   </body>
# </html>

# INLINE CSS
# <html>
#   <head>
#   </head>
#   <body>
#     <h1 style="color: blue;">Big Text</h1>
#   </body></html>

internal = '<html>\n<head>\n    <style>h1 { color:blue; }</style>\n</head>\n<body>\n    <h1>Big Text</h1>\n</body>\n</html>'
inlined = '<html><head>\n    \n</head>\n<body>\n    <h1 style="color: blue;">Big Text</h1>\n\n</body></html>'

assert inlined == css_inline.inline(internal)

#  inline multiple HTML documents with ...
# css_inline.inline_many([html1, html2, ...])

# Configuration Options allowed with ...
# ss_inline.CSSInliner(keep_style_tags=True).inline(html)
