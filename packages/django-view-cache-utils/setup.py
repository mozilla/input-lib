#!/usr/bin/env python
from distutils.core import setup

setup(
      name='django-view-cache-utils',
      version='0.1.1',
      author='Mikhail Korobov',
      author_email='kmike84@gmail.com',
      url='http://bitbucket.org/kmike/django-view-cache-utils/',      
      
      description = 'Django app that provides a method to do advanced view caching.',
      license = 'MIT license',
      packages=['view_cache_utils'],
      
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Plugins',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Natural Language :: Russian',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules'
        ],
)