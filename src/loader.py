import subprocess
import os
from config import GIT_REPO_DIR_PATH, GIT_REPO_URL, POSTS_REPO_NAME, SOURCE_DIRECTORY


def git_update():
    """
        Update the GIT database repo
    """
    try:
        import pdb;pdb.set_trace()
        if check_local_repo():
            os.chdir(GIT_REPO_DIR_PATH)
            git_pull()
            os.chdir(SOURCE_DIRECTORY)
        else:
            print('Some problem with the repo, repo doesnt exist')
    except Exception as e:
        raise e


def git_pull():
    """
        Run git clone at path
    """
    try:
        subprocess.call(['git', 'pull'])
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
