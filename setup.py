from distutils.core import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
setup(
  name = 'harpies',
  packages = ['harpies'],
  version = '1.0.0',
  license='MIT',
  description = 'Helps you generating link previews on the fly!',
  long_description=long_description,
  long_description_content_type='text/rst',
  author = 'S M Mahmudul Hasan',
  author_email = 'thegeek@iamlizu.com',
  url = 'https://iamlizu.com/tools/harpies/',
  download_url = 'https://github.com/IamLizu/harpies/archive/v_1_0_0.tar.gz',
  keywords = ['url', 'link', 'preview'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)