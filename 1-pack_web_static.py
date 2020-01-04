#!/usr/bin/python3

from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Generates a .tgz archive from the contents of web_static
    """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = 'versions/web_static_{}.tgz'.format(time)
    local("mkdir -p versions")
    cmd = local("mv " + archive_name + " ./versions/")
    if cmd.succeeded:
        return archive
    return None
