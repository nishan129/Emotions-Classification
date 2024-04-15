from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    This function resturns requirements
    """
    requirements_list: List[str] = []
    
    return requirements_list


setup(
    name= "EMOTIONS_CLASSIFICATION",
    version="0.0.0",
    description="",
    author= "Nishant Borkar",
    author_email="nishantborkar139@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
    
)