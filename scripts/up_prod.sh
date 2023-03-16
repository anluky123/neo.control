#!/bin/bash
docker-compose -f production.yml up --build -d --scale celeryworker=15
#--scale celeryworker=5