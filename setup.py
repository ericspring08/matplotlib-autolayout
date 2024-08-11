import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="matplotlib-autolayout",
    version="0.0.1",
    author="Eric Zhang",
    author_email="ericspring08@gmail.com",
    description="Auto layouts for matplotlib multiplots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ericspring08/matplotlib-autolayout",
    python_requires=">=3.6",
    packages=setuptools.find_packages(),
)
