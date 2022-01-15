"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "ANN-implementation-1"
USER_NAME = "pralaydas"
setuptools.setup(
    name=f"{PROJECT_NAME}-{USER_NAME}",
    version="0.0.1",
    author=USER_NAME,
    author_email="pralay.ceremorphic@gmail.com",
    description="it is an implementation of ANN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires = [
        "tensorflow",
        "matplotlib",
        "seaborn",
        "numpy",
        "pandas"
    ]
)
"""
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

PROJECT_NAME = "ANN-implementation-1"
USER_NAME = "pralaydas"
setup(
    name="src",
    version="0.0.1",
    author=USER_NAME,
    description="A small package for ANN Implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    author_email="pralay.ceremorphic@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        "tensorflow",
        "matplotlib",
        "seaborn",
        "numpy",
        "pandas"
    ]
)