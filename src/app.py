from flask import Flask, url_for, redirect, request, render_template, abort
from werkzeug.contrib.fixers import ProxyFix

from config import DEBUG_STATUS, HOST, PORT, GIT_REPO_SECRET
from loader import DataStore
from helper import hash_check


# Initilize Flask App
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

# Initilize Loading files from git repo
DS = DataStore()


@app.route('/update', methods=['POST'])
def reload_data():
    """
    When triggered by Github repo webhook, verifies if the request is valid and if it is,
     the data stored inside the git repo is pulled down and the DataStore is reloaded
    """
    if request.headers.get('X-Hub-Signature', None) is not None:
        gh_sha1 = request.headers.get('X-Hub-Signature')
        gh_payload = request.data
        secret = GIT_REPO_SECRET
        if hash_check(gh_sha1, gh_payload, secret):
            DS.reload()
        return 'Update successful'
    else:
        print('Recieved a post request to reload, but not from github')
        return abort(500)


@app.route('/')
def index():
    """
    Index view, a.k.a /root
    """
    return redirect('/blog')


@app.route('/blog/')
@app.route('/blog')
def blog_index_page():
    """
        Index of all blogposts
    """
    data = DS.get_metadata()
    return render_template('posts.html', content=data)


@app.route('/blog/<url_slug>/')
@app.route('/blog/<url_slug>')
def blog_post(url_slug):
    data = DS.get_data()
    metadata = DS.get_metadata()
    bp = {}

    # Search for metadata of the blogpost with that url
    bp = [item for item in metadata if item['url'] == url_slug]

    if not bp:
        # No such blogpost
        return redirect(url_for('blog_index_page'))
    else:
        # TODO: Decide how to handle multiple blog posts with the same title
            # Idea: During data load and throw an error if duplicate title is found
        bp = bp.pop(0)
        content = data[bp['file']]

        return render_template('post.html', content=content, metadata=bp)

if __name__ == "__main__":
    app.run(debug=DEBUG_STATUS, host=HOST, port=PORT)
