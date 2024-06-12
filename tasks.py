from invoke import task


@task
def upload(c):
    c.run("python -m twine upload dist/*")
