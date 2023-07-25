#!/bin/bash

#apt-get update && apt-get install -y cron python3 python3-pip jq curl
cd /app

pip install -r /app/requirements.txt

python3 power_checker.py

crontab /etc/cron.d/crontab.do

cron

tail -f /dev/null

