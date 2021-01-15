
# Generate Documentation via ReadtheDocs

This Section will guide you, in case that you want to create documentation with ReadtheDocs without installing Sphinx. 
To do so, create an account on Github and ReadtheDocs and follow the next steps.

## Creating/Fork a repository on GitHub

1. Creating repository on GitHub (see [Create a repo](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/create-a-repo)).

2. Fork this [Repository](https://github.com/nbayer2020/Simple-GitHub-repo-and-ReadTheDocs-set-up-Guide) (See [Fork a repo](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo) )

## After your repository was created:

.. note::

   If you used the option of **Fork**, you can avoid this step.

Add to your Github repository all the needed files that are required by ReadtheDocs to create a Documentation. 
The files (**ASCII Format**) that need to be copied/add to the repository, in order to create a Documentation with ReadtheDocs without installing sphinx:

### 1. Create the source/conf.py

The conf.py file is where you can configure all aspects of how your sources and builds reads your documentation.
In that file, which is executed as a Python source file, you assign configuration values

### 2. Create the readthedocs.yml

Read the Docs supports configuring your documentation builds with a YAML file. The configuration file must be in the root directory of your project.

All options are applied to the version containing this file. Below is an example YAML file which shows the one used for this site:
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

### 3. Create the requirements.txt

The requirements file option is useful for specifying dependencies required for building the documentation. 

To use the requirements file, create and place the requirements file in the root directory of your documentation directory. For example:
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

### 4. Create the source/index.rst

### 5. Create the source/images/TROPOS-Logo_ENG.png

## Conect to ReadtheDocs 

After all the files are in your repository go to [https://readthedocs.org/](https://readthedocs.org/) and create an acount and import your repository in **"Import a Project"**.

Then go to **"Import Manually"**:

* name:            set a Project name 
 
        (e.g. Simple-GitHub-repo-and-ReadTheDocs-set-up-Guide)                      
* repository URL:  https://github.com/ACCOUNT-NAME/REPOSITRY-NAME 

        (e.g. https://github.com/nbayer2020/Simple-GitHub-repo-and-ReadTheDocs-set-up-Guide)
* repository type: Git                                          

## Verificate if it works
After your Project was imported try **"Build version"**.

## ReadtheDocs Features 

1. ReadtheDocs allows autobuilding documentation for pull/merge requests for GitHub or GitLab projects. This triggers a new build when a new commit has been pushed to the Pull/Merge Request. You can enable it by:
   * Go to **"Admin"** > **"Advanced Settings"**
   * Enable the **"Build Pull Requests for this Project"** option

2. **Warning Banner for Pull/Merge Request Documentation:** While building documentation for pull/merge requests we add a warning banner at the top of those documentations to let the users know that this documentation was generated from pull/merge requests and is not the main documentation for the project.

3. **Send Build Status Notification:** We send build status reports to the status API of the provider (e.g. GitHub, GitLab). When a build is triggered for a pull/merge request we send build pending notification with the build URL and after the build has finished we send success notification if the build succeeded without any error or failure notification if the build failed.

## Last Step 

Now just click on **"Build version"** and wait for the latest version of your Documentation. 
Once the Documentation was sucsesfully build, you can start customuzing the content of your Documentation.
