#!/usr/bin/env python

import os

from cmdtree import command, entry


SRC_ROOT = os.path.dirname(
    os.path.realpath(__file__)
)
PROJECT_ROOT = os.path.dirname(
    SRC_ROOT
)

BIN_DIR = PROJECT_ROOT = os.path.join(
    PROJECT_ROOT,
    "bin"
)

USER_HOME = os.getenv("HOME", "/root/")

ALIAS_PATH = os.path.join(
    SRC_ROOT,
    "files/alias"
)
SHRC_PATH = os.path.join(
    SRC_ROOT,
    "files/shrc",
)
BASHRC = os.path.join(USER_HOME, ".bashrc")
ZSHRC = os.path.join(USER_HOME, ".zshrc")
PROFILE = os.path.join(USER_HOME, ".profile")


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


def _append2profile(source_str):
    if _in_file(PROFILE, source_str):
        print("`%s` already exists." % source_str)
        return
    _run("echo '%s' >> %s" % (source_str, PROFILE))


def install_alias():
    source_str = _get_source_str(ALIAS_PATH)
    _append2rc(source_str)


def init_ubuntu():
    """
    ubuntu only.
    """
    ub_init = os.path.join(
        SRC_ROOT,
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


def link_tools():
    if not os.path.exists(BIN_DIR):
        os.mkdir(BIN_DIR)
    script_dir = os.path.join(SRC_ROOT, "scripts")
    docker_dir = os.path.join(script_dir, "docker")
    git_dir = os.path.join(script_dir, "git-tools")
    for pdir in (docker_dir, git_dir):
        for script in os.listdir(pdir):
            full_path = os.path.join(pdir, script)
            dst = os.path.join(BIN_DIR, script)
            if os.path.exists(dst):
                continue
            os.symlink(
                full_path,
                dst,
            )
    path_str = "PATH=$PATH:%s" % BIN_DIR
    _append2profile(path_str)


@command("all")
def install_all():
    init_ubuntu()
    install_alias()
    mk_py_env()
    link_tools()


@command("link_tools")
def link():
    link_tools()

if __name__ == "__main__":
    entry()



















