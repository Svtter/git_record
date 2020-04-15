from invoke import task


@task
def commit(c):
    c.run('git add .')
    msg = input("Input your commit msg: ")
    c.run(f'git commit -m "{msg}"')
    c.run('git push')