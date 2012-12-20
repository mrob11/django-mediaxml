from distutils.core import setup

setup(
    name='django-mediaxml',
    version='0.1.0',
    author='Mike Robinson',
    author_email='mike.robinson.81@gmail.com',
    packages=['mediaxml',],
    url='http://github.com/mike360/django-notification-views/',
    license='BSD',
    description='Simple app to list files in a folder via xml.',
    long_description=open('README.md').read(),
    install_requires=[
        "Django >= 1.3",
    ],
)