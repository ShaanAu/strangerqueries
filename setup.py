from distutils.core import setup
import os
import codecs
from setuptools import setup

setup(
  name = 'strangerqueries',         # How you named your package folder (MyLib)
  packages = ['strangerqueries'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A package to allow users to run impala and hive queries within python without leaving there enviroment and connecting to a database', # Give a short description about your library
 long_description=open('README.rst').read(),
  author = 'Shaan Aucharagram',                   # Type in your name
  author_email = 'info@shaanaucharagram.com',      # Type in your E-Mail
  url = 'https://github.com/ShaanAu/strangerqueries',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ShaanAu/strangerqueries/archive/v_02.tar.gz',    # I explain this later on
  keywords = ['strangerqueries', 'hive', 'impala'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
          'subprocress'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
