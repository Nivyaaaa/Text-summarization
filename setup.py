import setuptools

with open("README.md", "r", encoding="utf-8")as f:
    long_description = f.read()

__version__= "0.0.0"

REPO_NAME= "Text-summarization"
AUTHOR_USER_NAME="Nivyaaa"
SRC_REPO="Text-summarization"
AUTHOR_EMAIL="nivyamraju@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="a small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https;//githum.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
    


)
