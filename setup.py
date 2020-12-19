import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pythonium-pkg-BGENINATTI", # Replace with your own username
    version="0.2.0a0",
    author="Bruno Geninatti",
    author_email="brunogeninatti@gmail.com",
    description="A space strategy algorithmic-game build in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bgeninatti/pythonium",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'Pillow',
        'matplotlib',
        'numpy',
        'attrs'],
    tests_require=['pytest'],
    setup_requires=['pytest-runner'],
    python_requires='>=3.6',
    scripts=['bin/pythonium'],
    data_files=[('font', ['font/jmh_typewriter.ttf'])]
)
