from setuptools import find_packages,setup
from typing import List

requirements_lst:List[str] =[]

def get_requirements()->List[str]:
    try:
        with open('requirements.txt','r') as file:
            files = file.readlines()
            for line in files:
                requirements = line.strip()
                if requirements and requirements!= '-e .':
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print(f'the file has not there')
    
    return requirements_lst



if __name__ == '__main__':
    result = get_requirements()
    print(f"Requirements found: {result}")

setup(
    name='Data_security',
    version='0.0.1',
    author='Taha Anik',
    author_email='tahaanik729@gmail.com',
    packages=find_packages(),
    libraries=get_requirements()
)
