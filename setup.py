import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="todo", # Replace with your own username
    version="0.0.1",
    author="Srujana",
    author_email="batch.srujana@gmail.com",
    description="Command Line Interface to manage todo lists",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nightKrwler/TODO-CLI",
    packages=setuptools.find_packages(),    
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Linux",
    ],
    python_requires='>=3.6',
)