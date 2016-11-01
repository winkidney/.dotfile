#!/bin/sh
sudo docker rm $(docker ps -a -q)
