from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='himage',
    version='0.1.2',
    description='A small library, of high level image processing tools',
    url='https://github.com/mySpecialUsername/highImage/',
    author='Gor G.',
    packages=find_packages(),
    install_requires=['numpy', 'opencv-python', 'matplotlib', 'PyQt6'],
    python_requires='>=3.6',
    zip_safe=False,
    long_description=long_description,
    long_description_content_type='text/markdown'
)
