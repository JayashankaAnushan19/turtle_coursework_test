#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def new_callback(receivedNewData):
    rospy.loginfo('New is - ' + rospy.get_caller_id() + receivedNewData.data)

def newListener():
    rospy.init_node('newListener', anonymous=True)
    rospy.Subscriber('newChatter', String, new_callback)
    rospy.spin()

if __name__ == '__main__':
    newListener()