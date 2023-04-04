import os
import io
import setuptools
    
def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("rewards", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content

def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]

setuptools.setup(
    name="rewardsAI",
    version="0.0.0.7",
    author="rewards-ai",
    description="Low-code RL agent training and evaluating platform.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/rewards-ai/rewards-sdk",
    python_requires='>=3.9',
    packages=setuptools.find_packages(exclude=["tests", ".github"]),
    include_package_data=True,
    package_data={
        'rewardsAI': ['assets/CarRace/*.png'],
    },
    install_requires=read_requirements("requirements.txt")
)