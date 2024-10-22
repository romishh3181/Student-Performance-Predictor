from setuptools import find_packages,setup
from typing import List
HYPHEN_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    list of requirements
    '''
    requiremnets=[]
    with open(file_path,'r') as obj:
        requirements= obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_DOT in requirements:
            requirements.remove(HYPHEN_DOT)
    return requirements        
    

setup(
name='mlproject',
version='0.0.1',
author='Rohan',
author_email='mavrohan2004@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)