from re import search

from setuptools import find_packages, setup

with open("src/squadmakers/challenge/__init__.py", "rt", encoding="utf8") as f:
    version = search(r"__version__ = \"(.*?)\"", f.read()).group(1)


setup(
    name="squadmakers-challenge",
    description="A project to solve a challenge",
    version=version,
    author="Gerson Carranza",
    author_email="g.carranzacord@gmail.com",
    url="https://github.com/dralh/squadmakers-challenge",
    packages=[
        "squadmakers." + pkg for pkg in find_packages(where="src/squadmakers")
    ],
    package_dir={"": "src"},
    install_requires=[
        "flask~=2.2.3",
        "SQLAlchemy~=2.0.9",
        " psycopg2-binary~=2.9.6",
        "PyYAML~=6.0.0",
        "arrow~=1.2.3",
        "requests~=2.28.2",
    ],
    extras_require={
        "dev": ["pytest~=7.3.1", "black~=23.3.0", "isort~=5.12.0"],
    },
    package_data={},
    python_requires=">=3.10",
)
