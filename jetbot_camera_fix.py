#!/usr/bin/env python
# get the camera stream of the /jetbot_camera/raw topic, reduce the resolution, flip it horizontally and vertically and publish it to the /jetbot_camera/image topic

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import matplotlib
matplotlib.use('Agg')

# use this counter to drop every X frames
# this is necessary because the camera stream is too fast for the jetbot to process
counter = 0

# define the callback function
def callback(data):
    # convert the image from ROS to OpenCV format
    try:
        cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
        print(e)
    
    # reduce the resolution
    cv_image = cv2.resize(cv_image, (640, 360))
    
    # flip the image horizontally and vertically
    cv_image = cv2.flip(cv_image, -1)
    
    # convert the image from OpenCV to ROS format
    try:
        image_message = bridge.cv2_to_imgmsg(cv_image, "bgr8")
    except CvBridgeError as e:
        print(e)
    
    global counter
    # if counter smaller than 10, drop the frame, else publish and reset the counter
    if counter < 10:
        counter = counter + 1
    else:
        counter = 0
        pub.publish(image_message)
        
# initialize the node
rospy.init_node('camera_fixed_topic', anonymous=True)

# initialize the publisher
pub = rospy.Publisher('/jetbot_camera/image', Image, queue_size=10)

# initialize the subscriber
sub = rospy.Subscriber('/jetbot_camera/raw', Image, callback)

# initialize the cv bridge
bridge = CvBridge()


# keep the node running
rospy.spin()


