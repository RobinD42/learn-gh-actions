import os
from invoke import task, run


VERSION="12.34"

def get_version():
    result = run('git rev-parse --short=8 HEAD', echo=False, hide=True)
    git_rev = result.stdout.strip()
    return f'{VERSION}-{git_rev}'


@task
def version(ctx):
    print(get_version())


@task
def build(ctx):
    os.makedirs('dist', exist_ok=True)
    file_name = f'dist/my-build1-{get_version()}.txt'
    with open(file_name, 'w') as f:
        f.write('This is just a dummy file to simulate having built something.\n')
        f.write(f'Version: {get_version()}\n')
    print(f'Created: {file_name}')


@task
def build2(ctx, os, pyver, arch):
    os.makedirs('dist', exist_ok=True)
    file_name = f'dist/my-build2-{get_version()}-{os}-{pyver}-{arch}.txt'
    with open(file_name, 'w') as f:
        f.write('This is just a dummy file to simulate having built something.\n')
        f.write(f'Version: {get_version()}\n')
        f.write(f'OS:      {get_version()}\n')
        f.write(f'PyVer:   {get_version()}\n')
        f.write(f'Arch:    {get_version()}\n')
    print(f'Created: {file_name}')
