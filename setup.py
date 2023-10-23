import setuptools
import os

setuptools.setup(

    name="SingularityCore",
    version="0.0.1",
    packages=[""],
    license="MIT",
    long_description="Python package to manage singularity files",
    scripts= [f"scripts/{x}" for x in os.listdir("scripts")],

)