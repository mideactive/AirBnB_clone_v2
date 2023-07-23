#!/usr/bin/python3
"""
Fabric script to generate a
.tgz archive from the contents of the web_static folder
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Compresses the contents of web_static folder into a .tgz archive
    and saves it in the versions directory.
    Returns the path to the created archive, or None if the archiving fails.
    """
    local("mkdir -p versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)
    result = local("tar -czvf {} web_static".format(archive_path))
    if result.succeeded:
        return archive_path
    else:
        return None
