# -*- coding: utf-8 -*-

name = "a_package_here"

version = "1.3.0"

build_command = "echo 'foo'"


def commands():
    import os

    env.PYTHONPATH.append(os.path.join("{root}", "python"))
