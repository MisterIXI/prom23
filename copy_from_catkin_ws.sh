#!/bin/bash
# copy and replace files from ~/catkin_ws/src to ~/workspace/prom23/catkin_ws/src

rsync -av --exclude='jetbot_ros' --exclude='ros_deep_learning' --exclude='ld08_driver' --exclude='turtlebot3' ~/catkin_ws/src/ ~/workspace/prom23/catkin_ws/src/



