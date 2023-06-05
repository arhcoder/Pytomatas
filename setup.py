from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="Pytomatas",
    version="1.1.3",
    packages=["Pytomatas"] or find_packages("src"),
    package_dir={"": "src"},
    author="arhcoder",
    author_email="arhcoder@gmail.com",
    description="Simulates Automatons Acceptors DFA, NFA, PDA and Turing Machines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arhcoder/Pytomatas",
    license="MIT License",
    include_package_data=True,
    project_urls={
        "Bug Tracker": "https://github.com/arhcoder/Pytomatas/issues",
        "Author": "https://github.com/arhcoder",
        "Source": "https://github.com/arhcoder/Pytomatas",
        "Contribution": "https://github.com/arhcoder/Pytomatas/pulls"
    },
    keywords=[
        "Automata", "Automaton", "Turing Machine", "Simulation",
        "DFA", "NFA", "PDA", "TM", "Python"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)