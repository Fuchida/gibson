# Gibson
Minimum effort git based blogging.

Building on the work from [snehesht/blog](https://github.com/snehesht/blog) and the styling from
my old blog [fuchida/blog](https://github.com/Fuchida/Archive/tree/master/blog.fuchida.me).

### Installation

```sh
  >> Git clone https://github.com/Fuchida/gibson.git
  >> pip install -r requirements.txt
```

Set Posts reository url and secrete password repo in `config.py`
or set them as environment variables.

```python
POSTS_GIT_REPO = None
POSTS_GIT_REPO_SECRET = None

# Example
# POSTS_GIT_REPO = 'https://github.com/fuchida/posts'
# POSTS_GIT_REPO_SECRET = '<Redacted>'
```

```sh
  >> python src/app.py
  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

