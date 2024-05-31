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
import os
import sys


# sys.path.insert(0, os.path.abspath("."))
# sys.path.insert(0, os.path.abspath(".."))
# sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(0, os.path.abspath("../../"))
sys.path.insert(0, os.path.abspath("../../core"))
sys.path.insert(0, os.path.abspath("../../components"))
sys.path.insert(0, os.path.abspath("../../eval"))
# sys.path.insert(0, os.path.abspath(".."))
# sys.path.insert(0, os.path.abspath("../core"))
# sys.path.insert(0, os.path.abspath("../components"))


# -- Project information -----------------------------------------------------

project = "LightRAG"
copyright = "2024, SylphAI"
author = "SylphAI"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinx.ext.autosectionlabel",
    # 'recommonmark',
    # 'myst_parser'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["tests", "test_*"]

# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.module.rst', '**/tests/*', '**/test_*.py', '*test.rst']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"


# These options are for the sphinx_rtd_theme
html_theme_options = {
    "collapse_navigation": False,
    "sticky_navigation": True,  # Ensures the sidebar stays at the top of the page
    "navigation_depth": 4,  # Controls how many headers are shown in the sidebar
    "includehidden": True,
    "titles_only": False,
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


def setup(app):
    app.add_css_file("custom.css")  # Add custom CSS file to the Sphinx configuration


# In Sphinx documentation, the configuration option add_module_names in the conf.py file controls
# whether module names are prefixed before object names in the documentation. This setting is particularly
# relevant when documenting Python modules and their contents, such as classes, functions, and methods.
add_module_names = False

autodoc_docstring_signature = True

# autodoc_default_options = {
#     "autosummary-no-titles": True,
#     "autosummary-force-inline": True,
#     "autosummary-nosignatures": True,
#     "members": True,
#     "private-members": False,  # (those starting with _).
#     "special-members": False,  # (those starting and ending with __).
#     "member-order": "bysource",
#     "show-inheritance": True,
#     # "undoc-members": True,
#     "autosectionlabel_prefix_document": True,
# }
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "member-order": "bysource",
    "show-inheritance": True,
    "private-members": False,  # Ensure this is True if you want to document private members
    "special-members": "__init__",  # Document special members like __init__
    "autosectionlabel_prefix_document": True,
}