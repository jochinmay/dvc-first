from certifi import where
from setuptools import setup,find_packages
from sqlalchemy import desc

with open("README.MD","r",encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="chinmayjoshi",
    description="A small testing package for dvc pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jochinmay/dvc-first",
    author_email="jochinmay94@gmail.com",
    package_dir={"":"src"},
    packages=find_packages(where="src"),license="GNU",
    python_requires=">=3.6",
    install_requires=['dvc','dvc[gdrive]','dvc[s3]','pandas','scikit-learn']
)