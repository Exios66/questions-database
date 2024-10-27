# Configuration file for the Sphinx documentation builder.
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'MVT Nexus'
copyright = '2024'
author = 'MVT Team'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Theme options
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False,
    'logo_only': False,
    'style_nav_header_background': '#2b2b2b',
}

# Custom CSS and JS
html_css_files = [
    'custom.css',
]

html_js_files = [
    'dark-mode.js',
]
