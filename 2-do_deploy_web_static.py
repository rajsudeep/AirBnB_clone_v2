#!/usr/bin/python3

from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['34.74.125.245', '34.73.79.111']


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

    print("All tasks succeeded!")
    return True
