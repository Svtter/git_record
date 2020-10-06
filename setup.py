import setuptools

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

setuptools.setup(
    name='git_record_svtter',
    version="0.0.2",
    author="svtter",
    author_email="svtter@qq.com",
    description="A tools to record temporal code",
    install_requires=requires,
    long_description=long_description,
    url="https://github.com/Svtter/git_record",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    extra_requires={
        'dev': dev_requires,
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'git_record.main': [
            'main = git_record.main'
        ]
    },
    python_requires=">=3.6",
)
