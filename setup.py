from setuptools import setup, find_packages

setup(
    name = "googleearthplot",
    version = "0.0.2",
    author = "Atsushi Sakai",
    author_email = "asakai.amsl@gmail.com",
    description = ("KML file generator for plotting on Google Earth"),
    license = "MIT",
    keywords = "google earth plot kml",
    url = "https://github.com/AtsushiSakai/googleearthplot",
    packages=find_packages(),
    install_requires = [
        "simplekml",
        "pandas",
        ],
)
