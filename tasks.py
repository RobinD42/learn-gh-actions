import os
from invoke import task, run


VERSION="12.34"


@task
def version(ctx):
    print(VERSION)

@task
def build(ctx):
    os.makedirs('dist', exist_ok=True)
    with open(f'dist/my_archive-{VERSION}.zzz', 'w') as f:
        f.write('This is just a dummy file to simulate having built something.')

