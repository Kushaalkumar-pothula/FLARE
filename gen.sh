#!/bin/bash

current_date_time="`date "+%Y-%m-%d %H:%M"`";
echo "Starting FLARE at $current_date_time:"

start_time="$(date -u +%s)"

python main.py

end_time="$(date -u +%s)"
elapsed="$(($end_time-$start_time))"

echo "Synthetic FRB catalog generated successfully in $elapsed seconds."
