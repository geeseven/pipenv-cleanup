#!/usr/bin/env python
from os import environ, listdir
from os.path import expanduser, isdir
from shutil import rmtree

# https://pipenv.pypa.io/en/latest/advanced/#custom-virtual-environment-location
try:
    pipenv_location = expanduser(environ["WORKON_HOME"])
except KeyError:
    pipenv_location = expanduser("~/.local/share/virtualenvs")

pipenv_envs = listdir(pipenv_location)

rm_pipenv_envs = []

for pipenv_env in pipenv_envs:
    env = pipenv_location + "/" + pipenv_env
    f = open(env + "/.project", "r")
    Path = f.read()
    if isdir(Path) is False:
        rm_pipenv_envs.append((Path, env))

if rm_pipenv_envs:
    print("Found the following deleted pipenv project homes.\n")
    for i in rm_pipenv_envs:
        print(i[0])
    print("\nDo you want to delete the corresponding pipenv virtualenvs?\n")
    for i in rm_pipenv_envs:
        print(i[1])
    if input("\n(y/N)") != "y":
        print("no action taken")
        exit()
    else:
        print("The pipenv virtualenvs have been deleted.")
        for i in rm_pipenv_envs:
            rmtree((i[1]))
else:
    print(
        "There are no deleted pipenv project homes that still have pipenv virtualenvs."
    )
