
# Generate Documentation via ReadtheDocs

In case that you want to create documentation with ReadtheDocs without installing Sphinx. To do so, create an account on Github and ReadtheDocs and follow the next steps.

## Creating/Fork a repository on GitHub

1. Creating repository on GitHub (See [Create a repo](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/create-a-repo)

2. Fork this [Repository](https://github.com/nbayer2020/Simple-GitHub-repo-and-ReadTheDocs-set-up-Guide) (See [Fork a repo](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo) )

## After your repository was created:

If you used the option of **fork**, you can avoid this step.

Create all the needed files that are required by ReadtheDocs to create a Documentation. 
The files (**ASCII Format**) that need to be copied/add to the repository, in order to create a Documentation with ReadtheDocs without installing sphinx:

* Makefile
* make.bat
* readthedocs.yml
* requirements.txt
* source/config.py
```
The conf.py file is where you can configure all aspects
of how your sources and builds reads your documentation.
In that file, which is executed as a Python source file,
you assign configuration values
```
* source/index.rst
* source/images/TROPOS-Logo_ENG.png

All this files should be copied from this [Repository](https://github.com/nbayer2020/Simple-GitHub-repo-and-ReadTheDocs-set-up-Guide)

## Conect to ReadtheDocs 

After all the files are in your repository go to [https://readthedocs.org/](https://readthedocs.org/) and create an acount and import your repository in **Import  a Project**.

Then go to **import Manually**:

* name:            set a Project name (e.g. Simple-GitHub-repo-and-ReadTheDocs-set-up-Guide)                      
* repository URL:  https://github.com/ACCOUNT-NAME/REPOSITRY-NAME (e.g. https://github.com/nbayer2020/Simple-GitHub-repo-and-ReadTheDocs-set-up-Guide)
* repository type: Git                                          

## Verificate if it works
After your Project was imported try **Build version**

## ReadtheDocs Features 

1. ReadtheDocs allows autobuilding documentation for pull/merge requests for GitHub or GitLab projects. This triggers a new build when a new commit has been pushed to the Pull/Merge Request. You can enable it by:
* Go to **Admin** > **Advanced settings**
* Enable the **Build pull requests for this project** option

2. **Warning Banner for Pull/Merge Request Documentation:** While building documentation for pull/merge requests we add a warning banner at the top of those documentations to let the users know that this documentation was generated from pull/merge requests and is not the main documentation for the project.

3. **Send Build Status Notification:** We send build status reports to the status API of the provider (e.g. GitHub, GitLab). When a build is triggered for a pull/merge request we send build pending notification with the build URL and after the build has finished we send success notification if the build succeeded without any error or failure notification if the build failed.

To create documents via Sphinx go to [next](https://simple-github-repo-and-readthedocs-set-up-guide.readthedocs.io/en/latest/docs_with_sphinx_and_rtd.html).
