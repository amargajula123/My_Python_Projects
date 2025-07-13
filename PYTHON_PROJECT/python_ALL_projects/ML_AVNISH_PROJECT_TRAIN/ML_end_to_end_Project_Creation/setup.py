from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.3"
AUTHOR="Amar"
DESCRIPTION="This is the 2025 ML project"

REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
   
    Description: This function is going to return list of requirement 
    mention in requirements.txt file

    return This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(), 
install_requires=get_requirements_list()
)

# find_packages() will search all the packages that you are created and its going to return that names
# in a formate of list
# -e . is also search for all the packages that you are created so we just uderstand we are installing
# external packages and internall packages
# NOTEe : we can not use '"-e ."' without creating "'setup.py'" file in setup.py only we have all
# the information regading version ,author,project name like that


