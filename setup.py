import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='sqlite_easy',
    packages=['sqlite_easy'],
    version='1.0.0',
    license='MIT',
    description='This library can you help you use sqlite3 much easier and faster.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Spark Drago',
    author_email='huzaifa.farooq05@gmail.com',
    url='https://github.com/SparkDrago05/sqlite_easy',
    download_url='https://github.com/SparkDrago05/sqlite_easy/archive/refs/tags/v1.0.tar.gz',
    keywords=['sqlite', 'sqlite3'],
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
