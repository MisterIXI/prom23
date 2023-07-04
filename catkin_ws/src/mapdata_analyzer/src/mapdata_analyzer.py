#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import Odometry
import sys

lidar_data = None
map_data = None
odom_data = None
has_printed = False
def lidar_callback(data):
    # Print the LIDAR data
    # print(data)
    global lidar_data
    lidar_data = data
    update_map()

def map_callback(data):
    # Print the map data
    # print(f"Position: {data.info.origin.position.x}, {data.info.origin.position.y} Heading: {data.info.origin.orientation.z}")
    # print("Position: " + str(data.info.position.x) + ", " + str(data.info.origin.position.y))
    # print("Heading: " + str(data.info.origin.orientation.z))
    global map_data
    map_data = data
    update_map()

def odom_callback(data):
    # Print the odometry data
    # print("Position: ("+str(data.pose.pose.position.x)+", "+str(data.pose.pose.position.y)+")")
    # print("Orientation: "+str(data.pose.pose.orientation))
    global odom_data
    odom_data = data
    update_map()


def update_map():
    global map_data
    global lidar_data
    global odom_data
    global has_printed
    if map_data is not None and lidar_data is not None and odom_data is not None and not has_printed:
        print("Map data: " + str(map_data))
        print("Lidar data: " + str(lidar_data))
        print("Odom data: " + str(odom_data))
        # print("Hello :)")
        has_printed = True        
        rospy.signal_shutdown('My package is shutting down')

def listener():
    # Initialize the node
    rospy.init_node('lidar_listener', anonymous=True)

    # Subscribe to the /scan topic
    rospy.Subscriber('/scan', LaserScan, lidar_callback)
    # subscribe to the map topic /map
    rospy.Subscriber('/map', OccupancyGrid, map_callback)
    # subscribe to the odometry topic /odom
    rospy.Subscriber('/odom', Odometry, odom_callback)
    # Spin until the node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()




