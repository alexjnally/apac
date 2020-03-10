from setuptools import setup
import versioneer

requirements = [
    'pandas', 'os', 'pyodbc', 'xlsxwriter'
]

setup(
    name='apac',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Alex's modules",
    license="MIT",
    author="Alex Nally",
    author_email='alexjnally@gmail.com',
    url='https://github.com/alexjnally/apac',
    packages=['apac'],
    entry_points={
        'console_scripts': [
            'apac=apac.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='apac',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
