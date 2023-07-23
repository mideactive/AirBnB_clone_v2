#!/usr/bin/python3
"""
Fabric script to distribute an
archive to web servers using do_deploy function
"""

from fabric.api import run, put, env
import os

env.hosts = ['54.167.84.232', '18.207.1.128']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        archive_dir = "/data/web_static/releases/{}".format(
            archive_name.split('.')[0])
        put(archive_path, "/tmp/{}".format(archive_name))
        run("mkdir -p {}".format(archive_dir))
        run("tar -xzf /tmp/{} -C {}".format(archive_name, archive_dir))
        run("rm /tmp/{}".format(archive_name))
        run("mv {}/web_static/* {}".format(archive_dir, archive_dir))
        run("rm -rf {}/web_static".format(archive_dir))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(archive_dir))
        print("New version deployed!")
        return True
    except FileNotFoundError:
        print("Archive file not found.")
        return False
    except Exception as e:
        print("An error occurred: {}".format(str(e)))
        return False
