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
        path = 'data/web_static/releases/'
        noExt = archive_path.split('.')[0]
        noPar = noExt.split('/')[1]
        tru = path + noPar
        try:
            put(archive_path, "/tmp")
            run("sudo mkdir -p {}".format(tru))
            run("sudo tar -xzf /tmp/{}.tgz -C {}".format(noPar, tru))
            run("sudo rm -f /tmp/{}.tgz".format(noPar))
            run("sudo rm /data/web_static/current")
            lin = "/data/web_static/releases/{}".format(noPar)
            run("sudo ln -sf {} /data/web_static/current".format(lin))
            return True
        except Exception as e:
            return False
    else:
        return False
