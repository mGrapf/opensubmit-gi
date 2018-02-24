#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../executor/'))

# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages']

source_suffix = '.rst'
master_doc = 'index'
project = 'OpenSubmit'
copyright = u'2018, Peter Tröger'
author = u'Peter Tröger'
language = "en"
exclude_patterns = ['formats', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = True

html_theme = "sphinx_rtd_theme"
html_favicon = '../web/opensubmit/static/images/favicon.ico'
html_logo = '../web/opensubmit/static/images/favicon-32x32.png'

napoleon_google_docstring = True
napoleon_numpy_docstring = False

