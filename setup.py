from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    requirements_lst: List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            for line in file:
                req = line.strip()
                if req and req != '-e .':
                    requirements_lst.append(req)
                    print(f"Added requirement: {req}")
            print(f"Total requirements found: {len(requirements_lst)}")
    except FileNotFoundError:
        print("requirements.txt not found")

    return requirements_lst


setup(
    name='Data_security',
    version='0.0.1',
    author='Taha Anik',
    author_email='tahaanik729@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()   # ✅ FIX
)
