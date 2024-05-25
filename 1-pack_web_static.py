#!/usr/local/bin/python3.8

from fabric.api import local, run, env
from datetime import datetime


def do_pack():
    t = datetime.now().strftime('%Y%m%d%H%M%S')
    try:
        local(f'tar -cvzf versions/web_static_{t}.tgz web_static')
        return ('versions/web_static_{t}.tgz')
    except Exception:
        return (None)
