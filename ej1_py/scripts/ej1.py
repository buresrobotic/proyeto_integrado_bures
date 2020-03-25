#!/usr/bin/env python
# license removed for brevity
import rospy #importamos los modulos necesarios
from std_msgs.msg import Int16

def ej1():
    pub = rospy.Publisher('contador', Int16, queue_size=0) #creamos el publicador
    rospy.init_node('contador', anonymous=True) #iniciamos el nodo
    while not rospy.is_shutdown():
        try:
            hello_str=int(input("Dame un numero ")) #pedimos un numero
            rospy.loginfo(hello_str) #lo mostramos en pantalla
            pub.publish(hello_str) #y lo publicamos
        except NameError:
            error="Eso no es un numero "
            rospy.loginfo(error)
            pub.publish(error)

if __name__ == '__main__':
    try:
        ej1()
    except rospy.ROSInterruptException:
        pass 
