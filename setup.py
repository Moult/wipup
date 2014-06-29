from setuptools import setup, find_packages

setup(
    name = "wipup",
    description = "Eadrax is a diary for your creations, that allows you to create from anywhere.",
    version = "0.1",
    license = "MIT",
    url = "http://wipup.org/",
    author = "Dion Moult",
    author_email = "dion@thinkmoult.com",
    packages = find_packages(),
    install_requires = [
        'uwsgi',
        'werkzeug',
        'pymysql',
        'pystache',
    ]
)
