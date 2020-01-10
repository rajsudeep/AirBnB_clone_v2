#!/usr/bin/python3

from fabric.api import local
from datetime import datetime

n = datetime.now()

def do_pack():
    """Packs web_static files into .tgz file"""

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = 'versions/web_static_' + time + '.tgz'
    local('mkdir -p versions')
    command = local("mv " + archive + " ./versions/")
    if command.succeeded:
        return archive
    return None
