# Configuration file

project = "API Reference"
copyright = "2020"
author = "Ekaterina Mekhnetsova"

extensions = ['breathe']
templates_path = ['_templates']
html_static_path = ['_static']

breathe_projects = {
    "example_API":"../xml/",
    }

import sys
import os

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

import sphinx_rtd_theme

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

if on_rtd:
    using_rtd_theme = True

# Theme options
html_theme_options = {
    # 'typekit_id': 'hiw1hhg',
    # 'analytics_id': '',
    # 'sticky_navigation': True,  # Set to False to disable the sticky nav while scrolling.
    'logo_only': True,  # if we have a html_logo below, this shows /only/ the logo with no title text
    'collapse_navigation': False,  # Collapse navigation (False makes it tree-like)
    # 'display_version': True,  # Display the docs version
    'navigation_depth': 4  # Depth of the headers shown in the navigation bar
}
