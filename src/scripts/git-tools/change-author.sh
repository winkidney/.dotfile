#!/usr/bin/env bash
git filter-branch --commit-filter '
    if [ "$GIT_AUTHOR_EMAIL" = ${1} ];
    then
        GIT_AUTHOR_NAME=${2};
        GIT_AUTHOR_EMAIL=${3};
        git commit-tree "$@";
    else
        git commit-tree "$@";
    fi' HEAD
