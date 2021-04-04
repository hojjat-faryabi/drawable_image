from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'drawable image creator'
LONG_DESCRIPTION = 'prepare images for use in android studio projects'

setup(
    name="drimage",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="hojjat-faryabi",
    author_email="hojjat.faryabi@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=['Pillow', 'click'],
    entry_points={
        'console_scripts': [
            'drimage = drimage.__main__:main'
        ]
    },
    keywords=['image', 'drawable', 'android', 'android-studio', 'drimage'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)
