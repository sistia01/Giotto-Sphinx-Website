# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
#import os
#import sys
#sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Giotto'
copyright = '2021, Ruben Dries, Qian Zhu, Huipeng Li, Rui Dong, Guo-Cheng Yuan'
author = 'Developed by Ruben Dries, Qian Zhu, Huipeng Li, Rui Dong, Guo-Cheng Yuan.'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
import sphinx_rtd_theme

extensions = ['sphinx.ext.autosectionlabel', 
'sphinx.ext.autodoc',
'sphinx_rtd_theme',
'sphinx_design',
'sphinx_copybutton',
'sphinx_toolbox', #fatal error
'sphinx_toolbox.shields', #fatal error
'sphinx_toolbox.github'
#'sphinxcontrib.spelling' #spell checker fatal error
]

# Configuration for sphinx_toolbox
github_repository = "Giotto"
github_username = "RubD" 

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []
suppress_warnings = ["Unknown directive type dropdown", 
'autosectionlabel.*']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_logo = "images/GiottoLogo.png"

html_theme_options = {
    'logo_only': True,
    'display_version': True,
    'navigation_depth': 4,
    #Toc Tree Options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'body_max_width': 'none'
}

html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }
html_css_files = ["css/theme_edits.css"]
panels_add_fontawesome_latex = True
panels_add_bootstrap_css = True

# Toc Tree options
navtree_root_links = True
navtree_shift = False

def setup(app):
    app.add_css_file("css/theme_edits.css")

#Link badges
def get_badge_inputs(text, cls: str = ""):
    return text, cls.split()

def get_link_badge_inputs(link, text=None, type="link", cls: str = "", tooltip=None):
    return link, text or link, type, cls.split(), tooltip

#Copy clipboard image 
#To use a different image for your copy buttons, do the following:
#Place the image in the _static/ folder of your site.
#Set the copybutton_image_path variable in your conf.py to be the path to your image file, relative to _static/.
#copybutton_image_path = "_static/AdditionalImages/copyclipboard.png"
