from setuptools import setup, find_packages

setup(
    name='telegram-function',  # Replace with your project's name
    version='0.1.0',
    packages=find_packages(),  # Automatically find the `Folder` package
    install_requires=[],  # Add any dependencies here
    author='Pamod Madubashana',
    author_email='pamodmadubashana2003@gmail.com',
    description='A short description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/pamodmadubashana/telegram_function',  # Replace with your GitHub project URL
    license='MIT',  # Replace with your license
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
