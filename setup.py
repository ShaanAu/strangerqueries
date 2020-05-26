import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='strangerqueries-ShaanAu',
    versions='0.0.1',
    author='Shaan Aucharagram',
    author_email='info@shaanaucharagram.com',
    description='A pacakge to run both Impala and Hive queries easily within Python whilst connecting to a database',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

        ],
    python_requires='>=3.6',


    )
