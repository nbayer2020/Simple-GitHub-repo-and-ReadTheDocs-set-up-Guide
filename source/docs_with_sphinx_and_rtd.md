# Generating docs via Sphinx and RtD

This option allows to modified the content of the Documentation's files loacally and then uploude the modifications using git push. The Documentation can be created/uploded only locally if it is desired.

## Local Sphinx Generator

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

## Add source files
Add your source **.rst** or **.md** files (e.g. NEW_FILE) into source directory inside, for example source. 
Now edit **index.rst** and add there **filenames.rst**. In my case:

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

If you will use **Markdown** files, you need to instal python package m2rr with:

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

On CentOs7 you will have to install the latex-packeges manually.

## ReadtheDocs configuration

Go to [ReadTheDocs](https://readthedocs.org/) and create an account there. 

Click on the dasboard and then on **"Import a Project"**. Name your project and add your git url inside **Repo**. 

      (e.g. https://github.com/USER_NAME/REPOSITORY_NAME)

Repository Type is **Git** and documentation **Sphinx Html**. Rest is basicaly optional. 

## Create the **requirements.txt** like:

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

      **It might be that you should change the version of some of the packeges**

## Create the **readthedocs.yml** like:

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

## Last Step 

Now just click on **"Build version"** and wait for the latest version of your Documentation. 
Once the Documentation was sucsesfully build, you can start customuzing the content of your Documentation.















