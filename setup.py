from setuptools import setup, find_packages
import os
import sys

_dir = os.path.dirname(os.path.realpath(__file__))

setup(
  name = 'google-play-api',
  packages = find_packages(exclude=["test"]),
  version = '0.0.1',
  description = '',
  author = 'Marco Montagna',
  author_email = 'marcojoemontagna@gmail.com',
  url = 'https://github.com/mmontagna/googleplay-api',
  download_url = '',
  keywords = [],
  classifiers = [],
  install_requires = [],
  entry_points = {
      'console_scripts': ['googleplay-download=googleplay.download:main']
  }
)