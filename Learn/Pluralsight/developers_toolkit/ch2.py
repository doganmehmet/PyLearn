# Managing Python Packages

# 2.3. How an installed package is found
# sys.path
    # list of directories searched for packages
    # first item : current directory ('.')
    # last item : site-packages

# site-packages
    # third-party packages are installed here
    # location depends on OS, Python version, installation procedure
    # will be somewhere inside your Python installation
    # may not even be called site-packages (i.e. Debian: dist-packages)


# 2.4. Python packaging: Current state of affairs

# how to create, distribute and install packages in a reliable way?
# lots of info on the web is outdated or contradictory
# multiple tools: distutils, setuptools, easy_install, ez_setup, pip
# multiple formats: egg, wheel, source dist

# Preferred tools
    # Python Packaging Authority (pyPA)

# Creating and distributing packages (pyPA suggests)
    # use setuptools
    # do not use distutils, because it is discountinued, merged into setuptools
    # do not use easy_install since it is included in setuptools

# Installing packages (pyPA suggests)
    # use pip
    # with virtualenv


# 2.8. Installing packages with pip

# installing a package
    # pip install requests
    # pip install requests == 1.0  -> for installing specific version
    # pip install 'requests >= 2.1' -> for installing higher version than some version
    # use quotes to prevent redirection with '>' and '<'

# removing a package
    # pip uninstall requests

# Be careful!
    # don't start installing a lot of packages.
    # better to install packages within virtual environments

# 2.9. Inspection packages with pip

# list all installed packages
    # pip list   -> will show the name and version for each installed packages

# get info on a specific package
    # pip show requests

# seach for a package
    # pip seach query

# pypi site : http://pypi.python.org/


# 2.10. Requirement files

# pip freeze > requirements.txt
    # save your project's dependencies in requirements.txt
    # including correct versions

# pip install -r requirements.txt
    # install all packages listed in requirements.txt


# 2.12. Resources

# Watch out!
    # There is a lot of outdated info on the web

# Python Packaging User Guide (http://goo.gl/8o4L4m)
    # https://packaging.python.org/
# Pip
# Python package index
