from setuptools import find_packages,setup
from typing import List

REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

# provide the list of external libarires
def get_requirements()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
    
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="yashwant ram",
    author_email="yash97r@gmail.com",
    # all code of folders will be converted into packages
    # every folder which contains __init.py__ file is a package
    packages=find_packages(), 
    install_requires=get_requirements(),
)