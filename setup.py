from setuptools import find_packages, setup # find packages will find all the packages which are being used by ml project 
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj.readlines() # The problem with this will be \n will be appended once the line changes
        requirements = [ req.replace("\n", " ") for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='MLProject',
    version='0.1',
    author='Utkarsh',
    author_email='shahiutkarsh28@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
    )


