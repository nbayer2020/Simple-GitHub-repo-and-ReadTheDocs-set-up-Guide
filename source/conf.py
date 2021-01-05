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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Documentation Guide'
copyright = '2020, Nicolas Bayer'
author = 'Nicolas Bayer'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = 'v0.1'


# -- General configuration---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = [
#]
# extensions from fabian
extensions = [
#    'recommonmark',
     'm2rr',
#    'sphinx.ext.autodoc',
#    'sphinx.ext.autosummary',
#    'sphinx.ext.napoleon'
]
#################

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Set master (rst file)
# The master toctree document.
master_doc = 'index'

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
#source_suffix = '.rst'

# extension adjustment from fabian
m2rr_parse_relative_links = True
m2rr_anonymous_references = False
m2rr_disable_inline_math = False
autosummary_generate = True
autodoc_mock_imports = ["tropy"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Add TROPOS Logo for the HTML page. 
html_logo = './images/TROPOS-Logo_ENG.png'

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    #'preamble': r'\usepackage{pmboxdraw} \usepackage[utf8x]{inputenc} ',
     
     'maketitle': r'''
        \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1

        \begin{titlepage}
            \centering

            \vspace*{40mm} %%% * is used to give space from top
            \textbf{\Huge {Documentation Guiede}}\\[20pt]

            \vspace{20mm}
            \begin{figure}[!h]
                \centering
                \includegraphics[scale=0.3]{source/images/TROPOS-Logo_ENG.png}
            \end{figure}
            \vspace{20mm}


            \Large {Nicolas Bayer}

            \vspace*{0mm}
            \small  Last updated : \today

        \end{titlepage}

        \clearpage
        \pagenumbering{roman}
        \tableofcontents
        \pagenumbering{arabic}

        ''',

}


