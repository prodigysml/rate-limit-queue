from setuptools import setup

setup(
    name='rate_limit_queue',
    version='0.1.0',
    description='A rate limited queue, allowing users to fetch items in accordance to the rate limit configured.',
    url='https://github.com/prodigysml/rate_limit_queue',
    author='Sajeeb Lohani',
    author_email='sajeeb@0dd.zone',
    license='BSD 2-clause',
    packages=['rate_limit_queue'],
    install_requires=[],

    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ],
)
