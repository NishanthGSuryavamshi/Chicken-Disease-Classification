# 1. create the template file for every projects, list out all the file name or folders required for the project.contains projects name shud be changed for other projects

import os
import sys
from pathlib import Path
import logging  # importing all required libraries

# configuring the logging facility
logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

# give the project name [should be changed for other projects]
project_name = "CNN Classifier"

# give the list of files or folders to be created.
list_of_files = [
    ".github/worlflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/models/__init__.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/configuration/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py",
    "templates/index.html",
]

# for loop for reading each filenames in the list of files
for filepath in list_of_files:
    # file path should be passed in to Path constructor so that path constructorreads its as a path
    filepath = Path(filepath)
    # split teh path into filenames and pale directory
    filedir, filename = os.path.split(filepath)

    if filedir != '':  # if filedir is not empty
        # create directory,ignore if it exists
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory {filedir}")

    # if file path doesnt exist or file size is zero
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:  # just create the file in the name of file path
            pass
            logging.info(f"Created empty file {filepath}")

    else:
        logging.info(f"File {filepath} already exists")
