'''
It typically contains information about the package, such as its name, version, and dependencies,
as well as instructions for building and installing the package.
'''

from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = "-e ."
def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file:
        '''
        This function will return the list of requirements
        '''
        requirements = []
        with open(file_path) as file:
            requirements = file.readlines()
            #requirements = [req.replace("\n", "") for req in requirements]
            requirements = [req.strip() for req in requirements]    # removes both spaces and \n. some extra spaces were there in requirements.txt file.
                                                                    # that caused error because it eliminated removing HYPEN E DOT from requirements
                                                                    # Ex: Requirements 2 : ['        numpy', '        pandas', '        seaborn', '        -e .    ']

            if(HYPEN_E_DOT in requirements):
                requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
    name="personality prediction project",
    version="0.1.0",
    author="Yasindu",
    author_email="liyanageyasindu01@gmail.com",
    description="A project to predict personality traits using machine learning.",
    packages=find_packages(),

    install_requires= get_requirements('requirements.txt')    

    )