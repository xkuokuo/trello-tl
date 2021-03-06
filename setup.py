from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='trello-tl',
    version='0.1.0',
    test_suite="tests",
    description='A Trello CLI tool.',
    long_description=readme,
    author='xkuokuo',
    author_email='xinkuo.dev@gmail.com',
    url='https://github.com/xkuokuo/trello-tl',
    license=license,
    install_requires=['requests'],
    entry_points={
        'console_scripts': ['tl=trello_tl.cli:main'],
    },
    packages=find_packages(exclude=('tests', 'docs'))
)
