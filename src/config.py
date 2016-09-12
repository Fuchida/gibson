import os

# Accepted file formats regex
# markdown accepted
# reStructuredText not accepted for now
ACCEPTED_FILE_FORMATS = "^.*\.md$"  # .md

POSTS_GIT_REPO = None
POSTS_GIT_REPO_SECRET = None

# Git Repo Config
# Fetched via environmental variables
GIT_REPO_URL = os.environ.get('POSTS_GIT_REPO', POSTS_GIT_REPO)

POSTS_REPO_NAME = GIT_REPO_URL.split('/')[-1].replace('.git', '')
SOURCE_DIRECTORY = os.getcwd()
GIT_REPO_DIR_PATH = os.path.join(SOURCE_DIRECTORY, POSTS_REPO_NAME)

GIT_REPO_SECRET = os.environ.get('POSTS_GIT_REPO_SECRET', POSTS_GIT_REPO_SECRET)

# Server Config
PORT = 5000
HOST = '0.0.0.0'
DEBUG_STATUS = False
