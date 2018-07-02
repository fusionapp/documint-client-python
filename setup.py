import os
import codecs
import versioneer
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(HERE, *parts), 'rb', 'utf-8') as f:
        return f.read()


setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    name='txdocumint',
    description='Twisted Python clj-documint client implementation',
    license='MIT',
    author='Jonathan Jacobs',
    author_email='jonathan@jsphere.com',
    url='https://github.com/fusionapp/txdocumint',
    platforms='any',
    long_description=read('README.rst'),
    packages=['txdocumint', 'txdocumint.test'],
    test_suite='txdocumint',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=[
        'twisted>=15.5.0',
        'treq>=15.1.0',
    ],
    extras_require={
        'dev': ['pytest>=2.7.1', 'testtools>=2.0.0'],
    },
)
