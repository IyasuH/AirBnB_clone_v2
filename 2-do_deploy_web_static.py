#!/usr/bin/python3
"""
Fabric script that distributes an archive to web server
using the function do_deploy
"""
from fabric.api import sudo, put, run, settings, env
import shutil
import os

env.hosts = ['34.139.86.96', '34.204.187.38']


def do_deploy(archive_path):
    """
    deploy
    """
    if os.path.exists(archive_path):
        try:
            put(archive_path, "/tmp/")
            nm = archive_path.partition('/')[2]
            nam = nm.partition('.')[0]
            name = "/data/web_static/releases/{}".format(nam)
            mn = "/tmp/{}".format(nm)
            run("shutil.unpack_archive(name, mn)")
            run("rm mn")
            run("rm /data/web_static/current")
            lin = "/data/web_static/releases/{}".format(nam)
            run("ln -sf lin /data/web_static/current")
            return True
        except Exception as e:
            return False
    else:
        return False
