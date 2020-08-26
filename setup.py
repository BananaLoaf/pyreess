# Local
from setuptools import setup, find_packages

# Project
from pyreess import PACKAGE_NAME, __version__, DESCRIPTION


with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()

setup(name=PACKAGE_NAME,
      version=__version__,
      install_requires=["seedrandom==2.2", "pyperclip"],
      packages=find_packages(),
      entry_points={
          "console_scripts": [
              "pyreess = pyreess.main:main"
          ]
      },

      # Metadata for PyPi
      author="BananaLoaf",
      author_email="bananaloaf@protonmail.com",
      # maintainer="BananaLoaf",
      # maintainer_email="bananaloaf@protonmail.com",
      license="MIT",

      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type="text/markdown",
      keywords=["deterministic", "password", "generator"],

      url="https://github.com/BananaLoaf/pyreess",
      # download_url=None,
      project_urls={
          "How secure is my password?": "https://howsecureismypassword.net"
      },

      # https://pypi.org/classifiers/
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3"
      ])
