# Copyright (C) 2022  Artyom Vancyan
# See full copyright notice at __init__.py
import subprocess

import setuptools

version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

assert "-" not in version
assert "." in version

# with open("README.md", "r", encoding="utf-8") as fp:
#     long_description = fp.read()

setuptools.setup(
    name="fuzzymap",
    version=version,
    author="Artyom Vancyan",
    author_email="artyom@pysnippet.org",
    description="",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/pysnippet/fuzzymap",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires=">=3.6",
    install_requires=[
        "fuzzywuzzy>=0.3.0",
        "python-Levenshtein>=0.12.1",
    ],
)
