#!/usr/bin/python3
# Creates and distributes an archive to web servers

from fabric.api import *
from os import path
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['34.74.125.245', '34.73.79.111']


def do_pack():
    """Packs web_static files into .tgz file"""

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = 'versions/web_static_' + time + '.tgz'
    local('mkdir -p versions')
    command = local("tar -cvzf " + archive + " web_static/")
    if command.succeeded:
        return archive
    return None


def do_deploy(archive_path):
    """Deploys archive"""
    if not path.exists(archive_path):
        return False
    ret_value = True
    a = put(archive_path, '/tmp/')
    if a.failed:
        ret_value = False
    arch = archive_path.replace(".tgz", "").replace("versions/", "")
    b = run('mkdir -p /data/web_static/releases/' + arch + '/')
    if b.failed:
        ret_value = False
    c = run('tar -xzf /tmp/' + arch + '.tgz' +
            ' -C /data/web_static/releases/' + arch + '/')
    if c.failed:
        ret_value = False
    d = run('rm /tmp/' + arch + '.tgz')
    if d.failed:
        ret_value = False
    e = run('mv /data/web_static/releases/' + arch +
            '/web_static/* /data/web_static/releases/' + arch + '/')
    if e.failed:
        ret_value = False
    f = run('rm -rf /data/web_static/releases/' + arch + '/web_static')
    if f.failed:
        ret_value = False
    g = run('rm -rf /data/web_static/current')
    if g.failed:
        ret_value = False
    h = run('ln -sf /data/web_static/releases/' + arch +
            '/' + ' /data/web_static/current')
    if h.failed:
        ret_value = False
    if ret_value:
        print("SUCCESS!")
    return ret_value


def deploy():
    """Distribute to all servers"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
