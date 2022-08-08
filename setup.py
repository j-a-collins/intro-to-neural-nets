import setuptools
import nnhelper

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="nnhelper",
    version=nnhelper.__version__,
    author="Jack Collins",
    author_email="jack.collins1@aviva.com",
    description="Package related to the Introduction Neural Networks notebook series",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/j-a-collins/nnhelper",
    project_urls={
        "Homepage": "https://stash",
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="nnhelper neural network networks python jupyter notebook",
    python_requires=">=3",
    install_requires=["numpy"],
    entry_points={
        "console_scripts": [
            "nnhelper = nnhelper.console.nnhelper:main",
        ]
    },
)
