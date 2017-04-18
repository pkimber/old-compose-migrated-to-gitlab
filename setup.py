import os
from distutils.core import setup


def read_file_into_string(filename):
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_readme():
    for name in ('README', 'README.rst', 'README.md'):
        if os.path.exists(name):
            return read_file_into_string(name)
    return ''


setup(
    name='kb-compose',
    packages=['compose', 'compose.management', 'compose.management.commands', 'compose.tests', 'compose.migrations', 'compose.urls'],
    package_data={
        'compose': [
            'static/*.*',
            'static/compose/*.*',
            'static/compose/css/*.*',
            'static/compose/font/*.*',
            'static/compose/font/liberation-sans/*.*',
            'static/compose/font/montserrat/*.*',
            'static/compose/font/roboto/*.*',
            'static/compose/img/*.*',
            'static/compose/js/*.*',
            'templates/*.*',
            'templates/compose/*.*',
        ],
    },
    version='0.0.34',
    description='compose',
    author='Malcolm Dinsmore',
    author_email='code-md@kbsoftware.co.uk',
    url='git@github.com:pkimber/compose.git',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django :: 1.8',
        'Topic :: Office/Business :: Scheduling',
    ],
    long_description=get_readme(),
)