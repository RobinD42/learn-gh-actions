import os
from invoke import task, run


VERSION="12.34"


@task
def version(ctx):
    result = run('git rev-parse --short=8 HEAD', echo=True)
    git_rev = result.stdout
    print(f'{VERSION}-{git_rev}')

@task
def build(ctx):
    os.makedirs('dist', exist_ok=True)
    with open(f'dist/my_archive-{version()}.zzz', 'w') as f:
        f.write('This is just a dummy file to simulate having built something.')

