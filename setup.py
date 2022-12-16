#!/usr/bin/env python
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def run_setup():
    setup(
        name='sql-queries',
        version='0.0.6',
        description='A tool to send SQL results to Graphite',
        keywords = 'SQL Graphite',
        author='Maria Paola Gonzalez',
        author_email='gonzahe2000@gmail.com',
        license='BSD',
        packages=['sql_to_graphite'],
        install_requires=[
            'sqlalchemy',
            'mysql-python',
        ],
        test_suite='tests',
        long_description=read('README.md'),
        zip_safe=True,
        classifiers=[
        ],
        entry_points="""
        [console_scripts]
        sql-to-graphite=sql_to_graphite:main
        """,
    )

if __name__ == '__main__':
    run_setup()