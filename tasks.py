import os
from invoke import task, run


VERSION="12.34"

def get_version():
    result = run('git rev-parse --short=8 HEAD', echo=False, hide=True)
    git_rev = result.stdout.strip()
    return f'{VERSION}-{git_rev}'

@task
def version(ctx):
    return get_version()

@task
def build(ctx):
    os.makedirs('dist', exist_ok=True)
    with open(f'dist/my_archive-{get_version()}.zzz', 'w') as f:
        f.write('This is just a dummy file to simulate having built something.')

