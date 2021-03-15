import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tesla-factory-package",
    version="0.0.1",
    author="Gediminas Šimavičius",
    author_email="gediminas.simavicius@gmail.com",
    description="Package for creating Tesla cars",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gedas-LT/tesla-factory-package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "tesla"},
    packages=setuptools.find_packages(where="tesla"),
    python_requires=">=3.6",
)