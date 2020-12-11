
# Generate docs without sphinx

In case that you want to create documents with ReadtheDocs without installing Sphinx.

## After creating the repository like in First steps:

Files you need to have in your repository, in order to create a Documenent with ReadtheDocs without installing sphinx:

* Makefile
* make.bat
* readthedocs.yml
* requirements.txt
* source/config.py
* source/index.rst
* source/images/

All this files should be copied from this [Repository](https://github.com/nbayer2020/ReadtheDocs-files)

## Create an account in ReadtheDocs 

After all thie files are in your repository go to [https://readthedocs.org/](https://readthedocs.org/) and create an acount and import your repository in **Import  a Project**.

Then go to **import Manually**:

* name:            set a Project name                           
* repository URL:  https://github.com/USER_NAME/REPOSITORY_NAME 
* repository type: Git                                          

## verificate if it works
After your Project was imported try **Build version**

To create documents with ReadtheDocs installing Sphinx go to [next](https://simple-github-repo-and-readthedocs-set-up-guide.readthedocs.io/en/latest/docs_with_sphinx_and_rtd.html).
