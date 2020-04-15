import os
import arrow
from git import Repo


class GitHandle:

    def __init__(self):
        git_repo_dir = os.getcwd()
        self.repo = Repo(git_repo_dir)
        assert not self.repo.bare

    def commit(self):
        pass

    def create_new_branch(self):
        """
        TODO[hao]: may need to use gitPython reconstruct
        Through this method to create new branch and save the source code to repo.
        """
        assert not self.repo.is_dirty()
        branch_name = arrow.now().format('YYYY-MM-DD-HH-mm-ss')
        os.system(f'git checkout -b "{branch_name}"')
        os.system(f'git push origin {branch_name}')
        os.system(f'git checkout master')


if __name__ == '__main__':
    gh = GitHandle()
    gh.create_new_branch()

