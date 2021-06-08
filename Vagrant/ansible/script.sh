#!/bin/bash

#cat ~/my_password.txt | docker login --username ddraiggoch --password-stdin

sudo docker-compose build

sudo docker-compose push
