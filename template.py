import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

ProjectName = "cnnClassification"

ListOfFiles = [
    ".github/workflows/.gitkeep",
    f"src/{ProjectName}/__init__.py",
    f"src/{ProjectName}/components/__init__.py",
    f"src/{ProjectName}/util/__init__.py",
    f"src/{ProjectName}/config/__init__.py",
    f"src/{ProjectName}/pipeline/__init__.py",
    f"src/{ProjectName}/config/configuration.py",
    f"src/{ProjectName}/entity/__init__.py",
    f"src/{ProjectName}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in ListOfFiles:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
