
# Generate docs via ReadtheDocs

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
* repository URL:  https://github.com/nbayer2020/ReadtheDocs-files
* repository type: Git                                          

## Verificate if it works
After your Project was imported try **Build version**

## ReadtheDocs Fetures 

1. Read the Docs allows autobuilding documentation for pull/merge requests for GitHub or GitLab projects. This triggers a new build when a new commit has been pushed to the Pull/Merge Request. You can enable it by:
* Go to **Admin** > **Advanced settings**
* Enable the **Build pull requests for this project** option

2. **Warning Banner for Pull/Merge Request Documentation:** While building documentation for pull/merge requests we add a warning banner at the top of those documentations to let the users know that this documentation was generated from pull/merge requests and is not the main documentation for the project.

3. **Send Build Status Notification:** We send build status reports to the status API of the provider (e.g. GitHub, GitLab). When a build is triggered for a pull/merge request we send build pending notification with the build URL and after the build has finished we send success notification if the build succeeded without any error or failure notification if the build failed.

To create documents via Sphinx go to [next](https://simple-github-repo-and-readthedocs-set-up-guide.readthedocs.io/en/latest/docs_with_sphinx_and_rtd.html).
