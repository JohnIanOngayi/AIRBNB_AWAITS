#!/usr/bin/python3

from fabric.api import run, env, task

env.hosts = ['local-web-01', 'local-web-02']


@task
def knowOs():
    run('uname -s')


@task
def knowHost():
    run('hostname')
