import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tesis_tools',
    version='0.1.1',
    author=['Jessica Nevárez Barrera'],
    author_email=["nebaje@ier.unam.mx"],
    description="New Package for elaborate graphics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['tesis_tools'],
    install_requires=['requests','pandas','numpy','datetime'],
)
