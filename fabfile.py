#!/usr/bin/python3

from fabric.api import roles, run, env, task

env.roledefs = {
    'web-01': {
        'hosts': ['local-web-01']
    },
    'web-02': {
        'hosts': ['local-web-02']
    }
}


@roles('web-01')
@task
def knowOs():
    run('uname -s')


@roles('web-02')
@task
def knowHost():
    run('hostname')
