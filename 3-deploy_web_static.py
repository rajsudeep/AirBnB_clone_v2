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
    if not archive_path:
        return False
    upload = put(archive_path, '/tmp/')
    if upload.failed:
        False
    archive = archive_path.replace(".tgz", "").replace("versions/", "")
    mkdir = run('mkdir -p /data/web_static/releases/' + archive + '/')
    if mkdir.failed:
        False
    tar = run('tar -xzf /tmp/' + archive + '.tgz' +
              ' -C /data/web_static/releases/' + archive + '/')
    if tar.failed:
        False
    rm1 = run('rm /tmp/' + archive + '.tgz')
    if rm1.failed:
        False
    mv = run('mv /data/web_static/releases/' + archive +
             '/web_static/* /data/web_static/releases/' + archive + '/')
    if mv.failed:
        False
    rm2 = run('rm -rf /data/web_static/releases/' + archive + '/web_static')
    if rm2.failed:
        False
    rm3 = run('rm -rf /data/web_static/current')
    if rm3.failed:
        False
    ln = run('ln -sf /data/web_static/releases/' + archive +
             '/' + ' /data/web_static/current')
    if ln.failed:
        return False

    print("SUCCESS!")
    return True


def deploy():
    """Distribute to all servers"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
