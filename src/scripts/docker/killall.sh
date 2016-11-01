#!/bin/sh
sudo docker kill $(sudo docker ps -a -q)
