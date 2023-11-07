from setuptools import setup, find_packages

setup(
    name='ObsidianTasker',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    author='Jakub Nowicki',
    author_email='q.nowicki@gmail.com',
    description='A small library to add tasks to markdown files for Obsidian',
    keywords='markdown obsidian tasks',
    entry_points={
        'console_scripts': [
            'obsidian_tasker=ObsidianTasker.main:main',
        ],
    }
)
