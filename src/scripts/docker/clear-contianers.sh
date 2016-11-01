#!/bin/sh

sudo docker ps -a | awk '{print $1}' | xargs --no-run-if-empty sudo docker rm
