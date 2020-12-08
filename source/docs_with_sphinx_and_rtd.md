# Generating docs with sphinx and RtD

1. Local sphinx generator

Install sphinx using pip and navigate yourself into git directory. Create docs folder there and go inside. Run:

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

2. Add your source **.rst** or **.md** files into some directory inside docs, for example source. Now edit index.rst and add there source/filenames.rst. In my case:

```rst
.. toctree::
   :maxdepth: 3

   source/intro
   source/nec_know
   source/domains_ip_servers
   source/ndg
   source/Arch
   source/RPi
```

If you will use **.md** files, you need to instal python package m2rr with:

```
pip install m2rr
```

You also need to modify the **conf.py** adding:

```python
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
```

3. Now just run:

```make html```  or ```make latexpdf```

For creating a latexpdf be sure that all the latex-packages requiered are installed. 
On Ubuntu xenial, the following packages need to be installed for successful PDF builds:

* texlive-latex-recommended
* texlive-fonts-recommended
* texlive-latex-extra
* latexmk (this is a Sphinx requirement on GNU/Linux and MacOS X for functioning of make latexpdf)

See: [https://www.sphinx-doc.org/en/master/usage/builders/index.html#sphinx.builders.latex.LaTeXBuilder](https://www.sphinx-doc.org/en/master/usage/builders/index.html#sphinx.builders.latex.LaTeXBuilder)
On CentOs7 you will have to install the latex-packeges manually

4. Read the Docs configuration

Go to the ReadTheDocs and create an account there.

Click on the dasboard and then on **import**. Name your project and add your git url inside **Repo**. In my case it’s:

```
https://github.com/USER_NAME/REPOSITORY_NAME
```

Repository type is **Git** and documentation **Sphinx Html**. Rest is basicaly optional. 

5. Create the requirements.txt like:

``` 
# docs/requirements.txt
Babel==2.8.0
imagesize==1.2.0
readme-renderer==26.0
Sphinx==3.1.2
sphinx-argparse==0.2.5
sphinx-rtd-theme==0.5.0
sphinxcontrib-applehelp==1.0.2
sphinxcontrib-devhelp==1.0.2
sphinxcontrib-htmlhelp==1.0.3
sphinxcontrib-images==0.9.2
sphinxcontrib-jsmath==1.0.1
sphinxcontrib-napoleon==0.7
sphinxcontrib-qthelp==1.0.3
sphinxcontrib-serializinghtml==1.1.4
m2rr==0.2.3 
m2r==0.2.1
```

Also add the **packeges names==version** that your document requires.

6. Create the readthedocs.yml like:

```
# readthedocs.yml
# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Build documentation in the docs/ directory with Sphinx
sphinx:
  configuration: source/conf.py
  fail_on_warning: true
  
# Build documentation with MkDocs
#mkdocs:
#  configuration: mkdocs.yml

# Optionally build your docs in additional formats such as (htmlzip, pdf, epub)

formats:
  - pdf
#  - htmlzip

# Optionally set the version of Python and requirements required to build your docs
python:
  version: 3.7
  install:
    - requirements: requirements.txt
```

See: [https://docs.readthedocs.io/en/stable/config-file/index.html](https://docs.readthedocs.io/en/stable/config-file/index.html)

Now just click on Create and wait.














