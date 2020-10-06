from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'gitpython',
    'arrow',
]

dev_requires = [
    'autopep8',
    'jedi',
    'pytest',
    'pynvim',
]

setup(
    name='git_record_svtter',
    version="0.0.1",
    author="svtter",
    author_email="svtter@qq.com",
    description="A tools to record temporal code",
    install_requires=requires,
    long_description=long_description,
    long_description_content_type="text/markdown",
    extra_requires={
        'dev': dev_requires,
    },
    entry_points={
        'git_record.main': [
            'main = git_record.main'
        ]
    },
    python_requires=">=3.6",
)
