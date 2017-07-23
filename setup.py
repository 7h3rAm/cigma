import os
from setuptools import setup, find_packages

setup(
  name = "cigma",
  version = "0.1",
  author = "Ankur Tyagi (@7h3rAm)",
  author_email = "7h3rAm@gmail.com",
  description = ("Cigma is a pure-Python file type identification library."),
  license = "Creative Commons Attribution-Noncommercial-Share Alike license",
  keywords = "common utils methods lib",
  url = "https://github.com/7h3rAm/cigma",
  packages = find_packages(),
  package_data = {
    "cigma": [
      "README.md",
      "magicbytes.json"
    ]
  },
  include_package_data = True,
  long_description = None,
  zip_safe = False,
  incstall_requires = [],
  classifiers = [
    "Development Status :: Alpha",
    "Topic :: Utilities",
    "License :: Creative Commons",
  ],
)
