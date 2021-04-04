from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'drawable image creator'
LONG_DESCRIPTION = 'prepare images for use in android studio projects'
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="drimg",
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="hojjat-faryabi",
    author_email="hojjat.faryabi@gmail.com",
    url="https://github.com/hojjat-faryabi/drawable_image",
    license='MIT',
    packages=find_packages(),
    install_requires=['Pillow', 'click'],
    entry_points={
        'console_scripts': [
            'drimg = drimg.__main__:main'
        ]
    },
    keywords=['image', 'drawable', 'android', 'android-studio', 'drimg'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)
