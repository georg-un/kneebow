from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='kneebow',
    version='1.0.0',
    packages=['kneebow'],
    url='https://github.com/georg-un/kneebow',
    license='MIT',
    author='Georg Unterholzner',
    author_email='georg.unterholzner.coding@gmail.com',
    description='Knee or elbow detection for curves',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['numpy', 'matplotlib', 'scikit-learn'],
    download_url='https://github.com/georg-un/kneebow/archive/v1.0.0.tar.gz',
    python_requires='>=3.4',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
