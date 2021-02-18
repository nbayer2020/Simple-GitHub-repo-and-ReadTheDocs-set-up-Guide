# Hello

.. note::
   
   If you don't want to install Sphinx or you just want to create a documentation via ReadtheDocs, skip this section.


Sphinx is a documentation generator or a tool that translates a set of plain text source files into various output formats, automatically producing cross-references, indices, etc. That is, if you have a directory containing a bunch of reStructuredText or Markdown documents, Sphinx can generate a series of HTML files, a PDF file (via LaTeX), man pages and much more.
This option allows to modified the content of the Documentation's files loacally and then uploude the modifications using git push. 
The Documentation can be created/uploded only locally if it is desired.

## Local Sphinx Generator

Install sphinx using pip and navigate yourself into git directory:
```
pip install sphinx
```

The root directory of a Sphinx collection of plain-text document sources is called the source directory. This directory also contains the Sphinx configuration file conf.py, where you can configure all aspects of how Sphinx reads your sources and builds your documentation.

Sphinx comes with a script called sphinx-quickstart that sets up a source directory and creates a default conf.py with the most useful configuration values from a few questions it asks you. To use this, run:

```
sphinx-quickstart
```

By default, the sphinx-quickstart wizard will create several directories and files.

```
_build           # The directory for containing Sphinx output
conf.py          # The file containing your project configurations
index.rst        # The master file containing the hierarchy of your documentation
make.bat         # A Windows command file
Makefile         # A file necessary for running the make command
_static          # The directory for static files, including custom stylesheets, pictures, etc.
_templates       # The directory for custom templates
```

## Add source files
Add your **.rst** or **.md** file (e.g. NEW_FILE) into /source directory. 
After that, edit **index.rst** and add there **filenames.rst**. In this site:

```rst
Documentation Guide
===================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   purpose
   read_the_docs
   docs_with_sphinx_and_rtd
   NEW_FILE
```

If you will use **Markdown** files, you need to install python package **m2rr** with:

```
pip install m2rr
```

You also need to modify the **conf.py** adding:

```python
...
extensions = [
#    'recommonmark',
     'm2rr',
#    'sphinx.ext.autodoc',
#    'sphinx.ext.autosummary',
#    'sphinx.ext.napoleon'
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

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
...
```

To see the complete **conf.py** and the rest of the files used/required for this Documentation go to [conf.py](https://github.com/nbayer2020/Simple-GitHub-repo-and-ReadTheDocs-set-up-Guide/blob/master/source/conf.py)

See also [Configuration options](https://www.sphinx-doc.org/en/master/usage/configuration.html).

## Produce Documents Locally

Now just run:

```make html```  or ```make latexpdf```

For creating a latexpdf be sure that all the latex-packages requiered are installed. 
On Ubuntu xenial, the following packages need to be installed for successful PDF builds:

* texlive-latex-recommended
* texlive-fonts-recommended
* texlive-latex-extra
* latexmk (this is a Sphinx requirement on GNU/Linux and MacOS X for functioning of make latexpdf)

See: [https://www.sphinx-doc.org/en/master/usage/builders/index.html#sphinx.builders.latex.LaTeXBuilder](https://www.sphinx-doc.org/en/master/usage/builders/index.html#sphinx.builders.latex.LaTeXBuilder)

On CentOs7 you will have to install some latex-packeges manually.

## Sphinx Features

* **Output formats:** HTML (including Windows HTML Help), LaTeX (for printable PDF versions), ePub, Texinfo, manual pages, plain text
* **Extensive cross-references:** semantic markup and automatic links for functions, classes, citations, glossary terms and similar pieces of information
* **Hierarchical structure:** easy definition of a document tree, with automatic links to siblings, parents and children
* **Automatic indices:** general index as well as a language-specific module indices
* **Code handling:** automatic highlighting using the Pygments highlighter
* **Extensions:** automatic testing of code snippets, inclusion of docstrings from Python modules (API docs), and more
* **Contributed extensions:** more than 50 extensions contributed by users in a second repository; most of them installable from PyPI

















