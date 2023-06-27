# Steps on how to connect and run the robot
1. Start the ROS Ubuntu master
1. Start the robot
    1. Unplug the HDMI port blocking USB cable
    1. Plug in the HDMI cable
    1. Switch it on
    1. Wait for the robot to boot and login
    1. Unplug the HDMI cable
    1. Plug the USB cable back in
1. Make sure configurations in the .bashrc are right
    1. In the Ubuntu master
        1. `export TURTLEBOT3_MODEL=waffle`
        1. `export ROS_MASTER_URI=http://[Ubuntu_IP]:11311`
        1. `export ROS_HOSTNAME=[Ubuntu_IP]`
    1. In the robot
        1. `export ROS_MASTER_URI=http://[Ubuntu_IP]:11311`
        1. `export ROS_HOSTNAME=[ROBOT_IP]`
1. In the ROS Ubuntu master
    1. Run `roscore` on the Ubuntu master
1. Connect into the robot with SSH
    1. Run `roslaunch turtlebot3_bringup turtlebot3_robot.launch` to run the LIDAR package
    1. Run `rosrun jetbot_ros jetbot_camera` to run the Jetbot camera package
    1. Run `rosrun jetbot_camera_fixed camera_fixed_topic.py` to run the custom camera package that fixes the camera topic
1. In the Ubuntu master 
    1. Run `roslaunch turtlebot3_slam turtlebot3_slam.launch` to run the SLAM package