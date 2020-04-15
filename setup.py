from setuptools import setup

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
    name='git_record',
    install_requires=requires,
    extra_requires={
        'dev': dev_requires,
    },
    entry_points={
        'git_record.main': [
            'main = git_record.main'
        ]
    }
)
