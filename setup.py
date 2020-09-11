import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="PyConsole-JasonTheDev",
    version="1.0.0",
    author="JasonTheDev",
    author_email="examqiename@gmail.com",
    description="A Tkinter GUI Console For Executing Commands.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)