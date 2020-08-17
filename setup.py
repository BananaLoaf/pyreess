# Local
from setuptools import setup, find_packages

# External
# Import numpy as np

# Project
from template import PACKAGE_NAME, __version__


with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()

# https://docs.python.org/2/distutils/setupscript.html
setup(name=PACKAGE_NAME,
      version=__version__,
      install_requires=["numpy"],
      packages=find_packages(),
      entry_points={
          "console_scripts": [
              "template = template.main:main",
              "template-again = template.main:main"
          ],
          "gui_scripts": [  # As far is I know they get detached from terminal
              "template = template.main:main"
          ]
      },

      # Metadata for PyPi
      author="BananaLoaf",
      author_email="bananaloaf@protonmail.com",
      # maintainer="BananaLoaf",
      # maintainer_email="bananaloaf@protonmail.com",
      license="MIT",

      description="This line is a description",
      long_description=LONG_DESCRIPTION,
      long_description_content_type="text/markdown",
      keywords=["template", "whatever"],

      url="https://github.com/BananaLoaf/setup-template",
      # download_url=None,
      project_urls={
          "Lord and Saviour": "https://stackoverflow.com/"
      },

      # https://pypi.org/classifiers/
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
      ])
