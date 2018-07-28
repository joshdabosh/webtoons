import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="webtoons",
    version="0.1.2",
    author="Joshua Wang",
    author_email="jwanggt@gmail.com",
    description="A small package for getting Webtoon comics for Python3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joshdabosh/webtoons",
    packages=setuptools.find_packages(),
    install_requires=(
        "bs4",
        "requests"
    ),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ),    
)
