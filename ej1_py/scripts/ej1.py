#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int16
def ej1():
    pub = rospy.Publisher('contador', Int16, queue_size=0)
    rospy.init_node('contador', anonymous=True) 
    while not rospy.is_shutdown():
        try:
            hello_str=int(input("Dame un numero "))
            rospy.loginfo(hello_str)
            pub.publish(hello_str)
        except NameError:
            error="Eso no es un numero "
            rospy.loginfo(error)
            pub.publish(error)
if __name__ == '__main__':
    try:
        ej1()
    except rospy.ROSInterruptException:
        pass 
