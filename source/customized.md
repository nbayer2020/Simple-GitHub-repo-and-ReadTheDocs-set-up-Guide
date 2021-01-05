# Customized your Documentation

In order to modify the content and the structure of your documentation you need to make some changes in the conf.py and index.rst files.
In order to do this you can change the .md files located in the /source directory or create new ones and add them to the index.rst file.

* To add a new content file (.md or .rst) save the new file and 
then add the new file in the index-rst without the files termination as:

```md
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

* You can also change the content by modifying the content from the .md files or delete the files from the index.rst to remoove the whole content from the Documentation.

