#!/usr/bin/env python

import rospy
from ejercicio4.msg import datos

def callback(msg):
    print msg

rospy.init_node("subscriptor")

sub=rospy.Subscriber("mensaje",datos,callback)
rospy.spin()
