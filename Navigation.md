## launching navigation with a map file
```bash
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/home/yannik/map_new.yaml```


## finding the ros locations
```bash
rospack find turtlebot3_navigation```

## changing speed values in the folders
/opt/ros/melodic/share/turtlebot3_navigation/param

## saving a map
```bash
# run slam node and run around manually to map the area
roslaunch turtlebot3_slam turtlebot3_slam.launch 
# run around with teleop
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
# run the map saver node 
rosrun map_server map_saver -f ~/map
```