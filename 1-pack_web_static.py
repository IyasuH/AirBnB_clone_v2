#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from the
contents of the web_static folder
"""
from fabric.api import local
import datetime
import os


def do_pack():
    """
    function to genrate .tgz file
    """
    now = datetime.datetime.now()
    name = "web_static_" + str(
            now.year) + '%02d' % now.month + '%02d' % now.day + str(
                    now.hour) + str(now.minute) + str(now.second)
    local("mkdir -p versions")
    print("Packing web_static to versions/{}.tgz".format(name))
    local("tar -czvf versions/{}.tgz web_static".format(name))
    try:
        f = open("versions/{}.tgz".format(name))
        f.close()
        path = os.path.relpath('versions/{}.tgz'.format(name), start=None)
        file_size = os.stat('versions/{}.tgz'.format(name)).st_size
        re = "versions/" + name
        rt = "web_static packed: {} -> {}Bytes".format(path, file_size)
        print(rt)
        return (re)
    except IOError:
        return (None)
