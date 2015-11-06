from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

__author__ = 'Tim Martin'

from setuptools import setup, find_packages

version = '1.0.0'


setup(
    author=__author__,
    author_email='tim.martin@vertical-knowledge.com',
    name='pycon-ripozo-tutorial',
    version=version,
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    description='A tutorial for ripozo; the tool for easily making RESTful interfaces',
    # long_description=long_description,
    install_requires=[
        'ripozo',
        'flask-ripozo',
        'flask',
        'ripozo-sqlalchemy',
        'requests',
        'SQLAlchemy',
        'pypermedia'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
        'console_scripts': [
            'helloworld = helloworld:main',
            'easy = easy_example:main',
            'full = full_example.app:main',
            'relationships = relationship_example:main'
        ]
    },
    extras_require={
        'docs': [
            'sphinx'
        ]
    },
    keywords='REST HATEOAS Hypermedia RESTful SIREN HAL API JSONAPI web framework',
    url='http://ripozo.readthedocs.org/'
)
