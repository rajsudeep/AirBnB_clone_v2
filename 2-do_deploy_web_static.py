#!/usr/bin/python3

from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['34.74.125.245', '34.73.79.111']


def do_deploy(archive_path):
    """distributes an archive to web servers"""

    if archive_path is None:
        return False

    upload = put(archive_path, '/tmp/')
    if upload.failed:
        return False
    archive = archive_path.replace('.tgz', '').replace('versions/', '')

    target = "/data/web_static/releases/" + filename[:-4]
    command = "mkdir -p " + target
    mkdir = run(command)
    if mkdir.failed:
        return False
    command = "sudo tar -zxf /tmp/" + filename + " -C " + target
    uncompress = run(command)
    if uncompress.failed:
        return False

    run('sudo rm /tmp/' + filename)
    run('sudo mv ' + target + '/web_static/* ' + target)
    run('sudo rm -rf ' + target + '/web_static')

    command = 'sudo ln -sf ' + target + ' /data/web_static/current'
    link = run(command)
    if link.failed:
        return False

    print("SUCCESS!")
    return True
