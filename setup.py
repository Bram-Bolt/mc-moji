from setuptools import setup, find_packages

setup(
    name="mc-moji",
    version="0.1.1",
    description="Create quick skin art based Minecraft skins.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Bram Bolt",
    author_email="bram@gelebeer.nl",
    url="https://github.com/yourusername/mc-moji",
    packages=find_packages(),
    install_requires=[
        "Pillow>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "mc-moji=app.cli:main",
        ],
    },
    package_data={
        "app": ["resources/mappings/beta/*", "resources/*.png"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
