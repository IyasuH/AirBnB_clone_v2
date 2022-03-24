#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from the
contents of the web_static folder
"""
from fabric.api import local
from fabric.api import execute
import datetime
import os


def do_pack():
    """
    function to genrate .tgz file
    """
    now = datetime.datetime.now()
    name = "web_static_" + str(now.year) + str(now.month) + str(
            now.day) + str(now.hour) + str(now.minute)
    local("mkdir -p versions")
    local("tar -czvf versions/{}.tgz web_static".format(name))
    try:
        f = open("versions/{}.tgz".format(name))
        f.close()
        path = os.path.relpath('versions/{}.tgz'.format(name), start=None)
        file_size = os.stat('versions/{}.tgz'.format(name)).st_size
        rt = "web_static packed: {} -> {}Bytes".format(path, file_size)
        print(rt)
        return(rt)
    except IOError:
        return(None)
