import os
import re
from setuptools import setup

base_path = os.path.dirname(__file__)

with open(os.path.join(base_path, 'CloudflareScraper', '__init__.py')) as fp:
    VERSION = re.compile(r'.*__version__ = "(.*?)"',
                         re.S).match(fp.read()).group(1)

setup(
  name = 'CloudflareScraper',
  packages = ['CloudflareScraper'],
  version = VERSION,
  description = 'This is an experimental update of Team Universal\'s UniversalScrapers\' cfscrape.py, which tries to solve a CF challenge with local Python code with as few imports as possible. ',
  author = ' doko-desuka',
  url = 'https://github.com/Arias800/CloudflareScraper',
  keywords = ['cloudflare', 'scraping'],
  include_package_data = True,
  install_requires = ['requests >= 2.0.0']
)
