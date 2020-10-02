#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callback(msg):
    print msg.data

rospy.init_node("subscriptor_numeros")

sub=rospy.Subscriber("un_numero",Int32,callback)
rospy.spin()
