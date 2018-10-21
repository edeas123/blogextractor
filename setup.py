import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='blogextractor',
    version='0.0.1',
    description='Extract data from blogs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/edeas123/blogextractor',
    author='Obaro Odiete',
    packages=setuptools.find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'flask'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
