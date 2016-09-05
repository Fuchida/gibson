import subprocess
import os
from config import GIT_REPO_DIR_PATH, GIT_REPO_URL, POSTS_REPO_NAME, SOURCE_DIRECTORY


def git_update():
    """
        Update the GIT database repo
    """
    try:
        if check_local_repo():
            os.chdir(GIT_REPO_DIR_PATH)
            subprocess.call(['git', 'pull'])
            os.chdir(SOURCE_DIRECTORY)
        else:
            print('Some problem with the repo, repo doesnt exist')
    except Exception as e:
        raise e


def get_current_dir():
    tmp = os.getcwd().split('/')
    return tmp[-1]


def git_clone():
    """
        GIT DATA repo doesn't exist, pull the repo
    """
    try:
        os.chdir(GIT_REPO_DIR_PATH)
        subprocess.call(['git', 'clone', GIT_REPO_URL])
    except Exception as e:
        raise e


def check_local_repo():
    """
        Check if git data repo exist
    """

    try:
        if POSTS_REPO_NAME not in os.listdir():
            subprocess.call(['git', 'clone', GIT_REPO_URL])
        else:
            return True
    except Exception as e:
        raise e
