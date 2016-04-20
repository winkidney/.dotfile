#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ALIAS_PATH="${DIR}/files/alias"
echo "Apply alias to file ~/.zshrc \n"
cat  >> ~/.zshrc
