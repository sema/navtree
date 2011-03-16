from setuptools import setup, find_packages
 
version = '1.0.0'
 
setup(
    name='navtree',
    version=version,
    description="Navigation system for Django projects.",
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='navigation,django',
    author='Casper S. Jensen',
    author_email='sema@semaprojects.net',
    url='https://github.com/sema/navtree',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
)
