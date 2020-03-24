#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int16

def callback(msg):
    rospy.loginfo("mensaje recibido: %s",msg.data)

def ej1():
    pub = rospy.Publisher('numeros3_1', Int16, queue_size=0)
    rospy.init_node('ej3_1', anonymous=True) 
    while not rospy.is_shutdown():
        try:
            hello_str=int(input("Dame un numero "))
            pub.publish(hello_str)
            global contador
            rospy.loginfo(contador)
            contador=contador+1
            if contador==5:
                rospy.Subscriber('numeros3_2',Int16,callback)

        except NameError:
            error="Eso no es un numero "
            rospy.loginfo(error)

if __name__ == '__main__':
    try:
        contador=0
        ej1()
    except rospy.ROSInterruptException:
        pass 