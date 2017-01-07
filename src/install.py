#!/usr/bin/env python

import os

PROJECT_ROOT = os.path.dirname(
    os.path.realpath(__file__)
)
USER_HOME = os.getenv("HOME", "/root/")

ALIAS_PATH = os.path.join(
    PROJECT_ROOT,
    "files/alias"
)
SHRC_PATH = os.path.join(
    PROJECT_ROOT,
    "files/shrc",
)
BASHRC = os.path.join(USER_HOME, ".bashrc")
ZSHRC = os.path.join(USER_HOME, ".zshrc")


def _get_source_str(file_path):
    return ". " + file_path


def _run(cmd):
    print(os.system(cmd))


def _in_file(file_path, string):
    with open(file_path, "r") as f:
        for line in f.readlines():
            if string in line:
                return True
    return False


def _append2rc(source_str):
    if _in_file(BASHRC, source_str):
        print("`%s` already exists." % source_str)
        return
    if os.path.exists(BASHRC):
        _run("echo %s >> %s" % (source_str, BASHRC))
    if os.path.exists(ZSHRC):
        _run("echo %s >> %s" % (source_str, ZSHRC))


def install_alias():
    source_str = _get_source_str(ALIAS_PATH)
    _append2rc(source_str)


def init_ubuntu():
    """
    ubuntu only.
    """
    ub_init = os.path.join(
        PROJECT_ROOT,
        "scripts/ub_init.sh"
    )
    _run(
        ub_init
    )


def mk_py_env():
    """
    make basic python development environment.
    :return:
    """
    packages_to_install = (
        "virtualenvwrapper",
    )
    for package in packages_to_install:
        _run(
            "sudo pip install {package}".format(package=package)
        )

    _append2rc(SHRC_PATH)


def install_all():
    init_ubuntu()
    install_alias()
    mk_py_env()


if __name__ == "__main__":
    install_all()



















