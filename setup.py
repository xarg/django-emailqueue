#!/usr/bin/env python
from setuptools import setup

setup(
    name='django-emailqueue',
    version='0.1',
    description='Django app for sending queued emails using cron',
    author='Alexandru Plugaru',
    author_email='alexandru.plugaru@gmail.com',
    url='http://github.com/humanfromearth/django-emailqueue',
    license='GPLv3',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    packages=['django_emailqueue'],
    requires=[
        'django (>=1.0)',
    ],
    entry_points = {
        'console_scripts':[
            'django_emailqueue_cron = django_emailqueue.cron:main'
        ]
    }
)
