#!/bin/bash

dir=~
[ "$1" != "" ]  && dir="$1" #引数があったらホームに変える

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg wifi_monitor.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Published Wi-Fi signal'
