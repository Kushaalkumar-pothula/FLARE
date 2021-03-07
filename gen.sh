#!/bin/bash

echo "______ _       ___  ______ _____ "
echo "|  ___| |     / _ \ | ___ \  ___|"
echo "| |_  | |    / /_\ \| |_/ / |__  "
echo "|  _| | |    |  _  ||    /|  __| "
echo "| |   | |____| | | || |\ \| |___ "
echo "\_|   \_____/\_| |_/\_| \_\____/ "

echo "Welcome to FLARE v2.0, now including optimized parallel processing and data loading mechanism. "
                                 
                                 
current_date_time="`date "+%Y-%m-%d %H:%M"`";
echo "Starting FLARE at $current_date_time:"

start_time="$(date -u +%s)"

python main.py

end_time="$(date -u +%s)"
elapsed="$(($end_time-$start_time))"

echo "Synthetic FRB catalog generated successfully in $elapsed seconds."
