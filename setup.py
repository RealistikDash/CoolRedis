from setuptools import setup

# Cython MUST be imported after setuptools.
from Cython.Build import cythonize

def parse_requirements() -> list[str]:
    with open("requirements.txt") as f:
        lines = f.readlines()

    return [
        line for line in lines
        if line and not line.startswith("#")
    ]

def read_readme() -> str:
    with open("README.md") as f:
        return f.read()

setup(
    name= "CoolRedis",
    version= "0.0.1",
    description= "A simple implementation of the Redis protocol.",
    license= "MIT",
    classifiers= [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Topic :: Database",
    ],
    python_requires=">=3.7",

    install_requires= parse_requirements(),

    url= "https://github.com/RealistikDash/CoolRedis",
    project_urls= {
        "GitHub: repo": "https://github.com/RealistikDash/CoolRedis",
        "GitHub: issues": "https://github.com/RealistikDash/CoolRedis/issues"
    },

    long_description_content_type= "text/markdown",
    long_description= read_readme(),

    ext_modules= cythonize(
        "coolredis/resp/*.pyx",
        annotate= True,
    )
)
