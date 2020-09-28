import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Hypyxel", 
    version="0.0.11",
    author="CraziiAce",
    author_email="teddyjraz@gmail.com",
    description="An easy-to-use python wrapper for the Hypixel API",
    long_description="# Hypyxel\nA python wrapper for the Hypixel API.\nI have a local branch with more endpoints.\n\nAs you can see, this is a WIP.\n\nPRs welcome, contrubuting guildelines coming soon.\n\n## Usage:\n\n`from hypyxel import hypixel`\n\n`hypixel.get_endpoints()`\n\n## Documentation:\n\nComing Soon!",
    long_description_content_type="text/markdown",
    url="https://github.com/CraziiAce/Hypyxel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL 3.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
