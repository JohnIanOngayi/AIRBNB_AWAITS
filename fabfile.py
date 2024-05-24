#!/usr/bin/python3

from fabric.api import cd, run, env, task
from fabric.utils import abort

env.hosts = ['local-web-01', 'local-web-02']


@task
def seeNginx():
    with cd('/etc/nginx/sites-enabled/'):
        run('cat default')
        run('echo "before abort"')
        abort('yeeeh budddddyyy!!!')
        run('echo "after abort"')
