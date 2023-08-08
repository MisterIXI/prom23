# PROM23 - Drunk turtles
This repository contains the source code and documentation for the project PROM23.  

# Manually installed packages on turtlebot
```shell
sudo apt-get install ros-melodic-teleop-twist-keyboard
```

# Quick start
### Start roscore
SSH into your server, adjust the bashrc if necessary with `nano ~/.bashrc`.
```bash
source /opt/ros/melodic/setup.sh
export TURTLEBOT3_MODEL=burger
export ROS_MASTER_URI=http://[ip_of_ros_server]:11311
export ROS_HOSTNAME=[ip_of_ros_server]
## use this one if you want to use X11 forwarding
# export DISPLAY=[ip_of_x11_target]:0
```
Now start the ros server with 
```bash
roscore
```
### Adjust the bashrc
When you connect, and any IPs changed, you have to adjust the bashrc and reconnect to the robot.
You can edit it with `nano ~/.bashrc`
```bash
source /opt/ros/melodic/setup.bash
source ~/catkin_ws/devel/setup.bash
export LDS_MODEL=LDS-02
export ROS_MASTER_URI=http://[ip_of_server]:11311
export ROS_HOSTNAME=[ip_of_robot]
export TURTLEBOT3_MODEL=burger
```
After editing the file you have to reconnect.
### LIDAR and rviz connection
To publish all base topic and read LIDAR data start the bringup node:
```bash
roslaunch turtlebot3_bringup turtlebot3_robot.launch
```
### Run yolo
To run yolo, you have to activate the correct venv and start the script with the workaround image.
```bash
cd yolov7
source venv3.6/bin/activate
python3 detect.py --weights yolov7-tiny.pt --conf 0.25 --img-size 1280 --no-trace --source Blank_16_9.jpg
```
This script does not clean up correctly. You can kill it with `ctrl+Z`, but you have to reboot after stopping this script again to free up the stuck memory.

### Open Rviz
To open rviz, connect to the server with ssh and open your X11 server if you want to use it and configured it.  
This version uses hector instead of normal gmapping since the odometry is broken.  
```bash
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=hector
```

### Start the camera script (not needed for yolo, just for viewing the camera)
The provided camera package will take the image from the jetcam package, flip it and drop a few frames to improve performance.  
Open two terminals and SSH into your robot with both.  
With one you start the normal jetbot camera package with:
```bash
rosrun jetbot_ros jetbot_camera
```

For the second one you have to start the custom package:
```bash
rosrun jetbot_camera_fixed camera_fixed_topic.py
```

### Show in RVIZ
To view the streams in RVIZ, you click on "Add" bottom left -> "By topic" tab in the top -> Select the correct Image source.  
For yolo it is: `/yolo/Image`  
For the normal camera stream it is: `/jetbot_camera/raw/Image`  
For the fixed camera stream it is: `/jetbot_camera/image/Image`