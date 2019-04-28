from setuptools import setup, find_packages

from os import path

here = path.abspath(path.dirname(__file__))
name = 'git-workshop'
version = '0.1'
release = '0.1.0'

setup(
    name=name,
    version=version,
    release=release,
    description='Git workshop',
    author='Eliad Hershkovitz',
    author_email='eliad.hershkovitz@briefcam.com',
    python_requires='>=3.6',
    include_package_data=True,
    packages=find_packages(),
    install_requires=['sphinx', 'sphinx_rtd_theme'],
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'release': ('setup.py', release),
            'source_dir': ('setup.py', 'docs')}},
)
