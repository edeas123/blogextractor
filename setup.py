import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='blogextractor',
    version='0.0.2',
    description='Crawl local blogs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/edeas123/blogextractor',
    author='Obaro Odiete',
    packages=setuptools.find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'bs4==0.0.1',
        'Flask==1.0.2',
        'Flask-RESTful==0.3.6',
        'lxml==4.2.4',
        'marshmallow==3.0.0b13',
        'PyYAML==3.13',
        'requests==2.19.1',
        'urllib3==1.23',
        'uwsgi==2.0.17.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
