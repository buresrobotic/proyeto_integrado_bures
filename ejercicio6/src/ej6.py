#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node("numeros")
pub=rospy.Publisher("un_numero",Int32,queue_size=1)
rate=rospy.Rate(2)

while not rospy.is_shutdown():
    try:
        numero=int(input("Dame un numero "))
        pub.publish(numero)
    except:
        pass
    
    rate.sleep()
