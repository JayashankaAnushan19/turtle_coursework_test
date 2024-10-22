#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def newTalker():
    pub = rospy.Publisher('newChatter', String, queue_size=10)
    rospy.init_node('newTalket', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        newString = 'New my Code %s' % rospy.get_time()
        rospy.loginfo(newString)
        pub.publish(newString)
        rate.sleep()

if __name__ == '__main__':
    try:
        newTalker()
    except rospy.ROSInterruptException:
        pass
