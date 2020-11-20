# pipenv-cleanup

This is a script I use to clean up [pipenv][0] virtualenvs for pipenv project homes that I deleted before deleting the virtualenvs.


## what you should do
```console
$ mkdir something
$ cd something
$ pipenv install foo bar foo-bar
...
$ vim something.py
$ pipenv run python something.py
Hello World!
$ # A few hours later
$ pipenv --rm
$ cd ../
$ rm -rf something
```

## what you actually do
```console
$ mkdir investigating-something
$ cd investigating-something
$ pipenv install foo bar foo-bar
...
$ vim pipenv investigating-something.py
$ pipenv run python investigating-something.py
Hello World!
$ # A few hours later
$ cd ../
$ rm -rf investigating-something
```
## time to clean up
```console
$ /path/to/pipenv-cleanup.py 
Found the following deleted pipenv project homes.

/home/user/investigating-something

Do you want to delete the corresponding pipenv virtualenvs?

/home/user/.local/share/virtualenvs/investigating-something-u88ilH1J

(y/N)n
no action taken
$ /path/to/pipenv-cleanup.py 
Found the following deleted pipenv project homes.

/home/user/investigating-something

Do you want to delete the corresponding pipenv virtualenvs?

/home/user/.local/share/virtualenvs/investigating-something-u88ilH1J

(y/N)y
The pipenv virtualenvs have been deleted.
$ /path/to/pipenv-cleanup.py 
There are no deleted pipenv project homes that still have pipenv virtualenvs.
```

[0]: https://github.com/pypa/pipenv
