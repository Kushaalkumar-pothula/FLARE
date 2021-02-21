#!/bin/bash

echo "Starting FLARE at:"
current_date_time="`date "+%Y-%m-%d %H:%M"`";
echo $current_date_time;

python energy.py &
python distance.py &
wait
python fluence.py
wait
python fluence_x_rays.py &
python fluence_analysis.py &

echo "Synthetic FRB catalog generated successfully."