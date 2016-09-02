# Gibson
Minimum effort developer blogging.

Building on the work from [snehesht/blog](https://github.com/snehesht/blog) and the styling from
my old blog [fuchida/blog](https://github.com/Fuchida/Archive/tree/master/blog.fuchida.me).

Gibson uses markdown files and git to build a simple blog. A developer that just want to
to push to a repo to update their blog, Gibson should be an ideal option.

### Installation

```sh
  >> Git clone https://github.com/Fuchida/gibson.git
  >> pip install -r requirements.txt
```

Set the repository url with your .md posts and secrete password in `config.py`
or set them as environment variables.

Also be sure to point your POST repo webhook setting to youblog.com/update

```python
POSTS_GIT_REPO = None
POSTS_GIT_REPO_SECRET = None

# Example
# POSTS_GIT_REPO = 'https://github.com/fuchida/posts'
# POSTS_GIT_REPO_SECRET = '<Redacted>'
```

```sh
  >> python src/app.py
  ...
  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

![Screenshot](docs/images/main_page.png)
