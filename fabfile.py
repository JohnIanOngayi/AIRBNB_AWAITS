#!/usr/bin/python3

from fabric.api import cd, run, env, task

env.hosts = ['local-web-01', 'local-web-02']


@task
def seeNginx():
    with cd('/etc/nginx/sites-enabled/'):
        run('cat default')
