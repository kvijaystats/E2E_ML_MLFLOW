
# Giving error when installing from pip.install, so remove before setting up new project
import setuptools

with open('README.md', 'r', encoding="utf-8") as f:
    long_description= f.read()


__version__== "0.0.0"

REPO_NAME=  "E2E_ML_MLFLOW"
AUTHER_USER_NAME= "kvijaystats"
SRC_REPO= "ml_project"
AUTHER_EMAIL= "kvijaystats@gmail.com"



setuptools.setup(
    name= SRC_REPO,
    version=__vsersion__,
    author= AUTHER_USER_NAME,
    author_email= AUTHER_EMAIL,
    description= "a small python package for ml app",
    long_description= long_description,
    long_description_content= 'text/markdown',
    url= f"https://github.com/{AUTHER_USER_NAME/{REPO_NAME}}",
    project_urls= {
        "BUG Tracker": f"https://github.com/{AUTHER_USER_NAME/{REPO_NAME}}/issues",
    },
    package_dir={"": "src"}
    packages= setuptools.find_packages(where= "src")
)
