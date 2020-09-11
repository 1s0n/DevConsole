import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyConsole-pkg-JasonTheDev", # Replace with your own username
    version="0.0.1",
    author="JasonTheDev",
    author_email="jasonbnps@gmail.com",
    description="A Tkinter GUI Console For Executing Commands.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: FREEWARE",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)