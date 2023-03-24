#!/bin/bash
docker-compose -f production.yml up --build -d && docker cp ./elopub/static/ $(docker-compose -f production.yml ps -q django):/app/elopub/

