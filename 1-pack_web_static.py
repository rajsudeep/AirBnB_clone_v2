#!/usr/bin/python3

from fabric.api import local
from datetime import datetime


n = datetime.now()


def do_pack():
    """Packs web_static files into .tgz file"""

    file_name = 'versions/web_static_{}{}{}{}{}{}.tgz'\
                .format(n.year, n.month, n.day, n.hour, n.minute, n.second)
    local('mkdir -p versions')
    command = local("tar -cvzf " + file_name + " ./web_static/")
    if command.succeeded:
        return file_name
    return None
