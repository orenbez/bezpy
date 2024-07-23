# Requires `pip install GitPython``
# also see pygit
# https://gitpython.readthedocs.io/en/stable/
import os 

from git import Repo

repo_folder = '../../data_external/repo_name'

if os.path.isdir(repo_folder):   # if repo exists, pull newest data 
    repo = Repo(repo_folder)
    repo.remotes.origin.pull()
else:                            # otherwise, clone from remote
    repo = Repo.clone_from('https://github.com/CSSEGISandData/COVID-19.git',  repo_folder)   

repo.working_dir

