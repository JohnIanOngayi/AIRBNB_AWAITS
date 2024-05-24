#!/usr/bin/python3

from fabric.api import cd, run, env, task
from fabric.contrib.console import confirm

env.hosts = ['local-web-01', 'local-web-02']


@task
def seeNginx():
    with cd('/etc/nginx/sites-enabled/'):
        confirm('Would you like to start: ', default=True)
        run('echo "Command 1')
        confirm('Would you like to proceed: ', default=True)
        run('echo "Command 2')
        confirm('Would you like to proceed: ', default=True)
        run('echo "Command 3')
