#!/usr/bin/python3
"""Fabric script to generate a .tgz archive from the contents of the web_static folder"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Function to generate a .tgz archive from the contents of the web_static folder"""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    result = local("tar -cvzf {} web_static".format(file_name))
    if result.succeeded:
        return file_name
    return None
