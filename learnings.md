# X11 forwarding
To forward RVIZ and other windows from the Ubuntu Master to the Host Machine.
If everything is set up correctly you have to do the following steps:
1. On the Ubuntu Master, run `export DISPLAY=[Host Machine]:0`
### Windows
1. On the Host Machine, run XLaunch
    1. Select "One large window"
    1. Disable Access Control
    1. Select "Start no client"


# Robot specificiations
- Don't run the robot while it's charging
- Don't unplug the USB cable of the board. Only the LIDAR is okay to unplug
- Wait until the robot is signed in and the Desktop is visible before unplugging the HDMI cable

# Create catkin rospy packages
1. `cd ~/catkin_ws/src`
1. `catkin_create_pkg [package_name] rospy`

# Potential problem with robot not connecting to rviz correctly
Change to a different wifi network and try again.