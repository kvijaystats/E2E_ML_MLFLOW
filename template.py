import os
from pathlib import Path
import logging

logging.basicConfig(level= logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name= 'ml_project'

# list of files

file_list= [
    ".github/workflows/.gitkeep",
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/entity/config_entity.py',
    f'src/{project_name}/constraints/__init__.py',
    'config/config.yaml',
    # 'dvc.yaml',
    'params.yaml',
    'schema.yaml',
    'main.py',
    'app.py',
    'Dockerfile',
    'requirments.txt',
    'setup.py',
    'research/trials.ipynb',
    'template.html'
]

for filepath in file_list:
    filepath= Path(filepath)
    filedir, filename= os.path.split(filepath)

    if filedir != "":
         os.makedirs(filedir, exist_ok=True)
         logging.info(f'creating directory;{filedir} for file: {filename}')

    if (not os.path.exists(filepath) or (os.path.getsize(filepath)== 0)):
        with open(filepath, 'w') as f:
            pass
        logging.info(f'Creating emplty file: {filepath}')
                     
    else:
        logging.info(f'{filename} is already exist')
    
    
    

