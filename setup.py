# coding=utf-8

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='binstruct',

    version="0.1.0",
    description=(
        'an advanced binary file structure parser/reader'
    ),
    long_description=open('README.md', 'r').read(),
    long_description_content_type="text/markdown",
    author='Qiufeng54321',
    author_email='williamcraft@163.com',
    maintainer='Qiufeng54321',
    maintainer_email='williamcraft@163.com',
    license='MIT License',
    packages=find_packages(),
    platforms=["ubuntu",'linux','unix', 'windows'],
    url='https://github.com/qiufeng54321/binstruct',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[]
)