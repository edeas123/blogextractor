import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='blogcrawler',
    version='0.0.1',
    description='Crawl local blogs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/edeas123/blogcrawler',
    author='Obaro Odiete',
    packages=setuptools.find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'flask'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)