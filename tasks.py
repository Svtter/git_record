from invoke import task


@task
def commit(c):
    c.run('git add .')
    msg = input("Input your commit msg: ")
    c.run(f'git commit -m "{msg}"')
    c.run('git push')


@task
def build(c):
    c.run("python setup.py sdist bdist_wheel")


@task
def upload(c):
    c.run("python -m twine upload dist/*")