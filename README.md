# testdeepextra
A test repo for https://github.com/kennethreitz/pipenv/issues/875

Testing with `pip-tools`:

```
$ pip install git+https://github.com/jazzband/pip-tools.git#egg=pip-tools
$ pip-compile --rebuild -nv requirements_straight.in
$ pip-compile --rebuild -nv requirements_extra.in
```
