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
            git_pull(GIT_REPO_DIR_PATH)
            os.chdir(SOURCE_DIRECTORY)
        else:
            print('Some problem with the repo, repo doesnt exist')
    except Exception as e:
        raise e


def git_pull(path):
    """
        Run git clone at path
    """
    try:
        subprocess.call(['git', 'clone', path])
    except Exception as e:
        raise e


def git_clone(path):
    """
        Run git clone at path
    """
    try:
        subprocess.call(['git', 'clone', path])
    except Exception as e:
        raise e


def check_local_repo():
    """
        Check if git data repo exist
    """

    try:
        if POSTS_REPO_NAME not in os.listdir():
            git_clone(GIT_REPO_URL)
        else:
            return True
    except Exception as e:
        raise e
