from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="Pytomata",
    version="1.6.0",
    author="arhcoder",
    author_email="arhcoder@gmail.com",
    description="Simulates Automatons Acceptors DFA, NFA, PDA and Turing Machines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arhcoder/Pytomata",
    license="MIT License",
    packages=find_packages(),
    include_package_data=True,
    project_urls={
        "Bug Tracker": "https://github.com/arhcoder/Pytomata/issues",
        "Contribution": "https://github.com/arhcoder/Pytomata/pulls"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    package_dir={"": "src"},
    python_requires=">=3.6"
)