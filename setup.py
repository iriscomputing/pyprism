from setuptools import setup, find_packages

setup(
    name="pyprism-crystallizer",
    version="1.0.0",
    description="Hermetic Python virtual environment crystallizer and single-file executable packager.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Vanguard Frontier Labs",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Build Tools",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "pyprism=pyprism.cli:main",
        ],
    },
)
