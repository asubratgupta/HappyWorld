import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="subratgupta", # Replace with your own username
    version="0.0.143",
    author="Subrat Gupta",
    author_email="subrat.iiit@gmail.com",
    description="This is for someone Special!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asubratgupta/HappyWorld",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)