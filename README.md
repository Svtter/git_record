# Git record

Use git branch to record temporal result.


## Install

`python setup.py install` or `pip install -e .`


## Call

``` python
from git_record.git_record import GitHandle

gh = GitHandle()
gh.create_new_branch()

```

This scripts will create a branch named `current date`.