#!/usr/bin/env python
# license removed for brevity
import rospy #importamos los modulos necesarios
from std_msgs.msg import Int16

def callback(msg): #creamos una funcion que reciba el mensaje y lo muestre por pantalla
    rospy.loginfo("mensaje recibido: %s",msg.data)

def memory_subscriber(): #funcion principal
    rospy.init_node('suscriptor_ej2',anonymous=True) #creamos el nodo
    rospy.Subscriber('contador',Int16,callback) #creamos el suscriptor
    rospy.spin() #hacemos que el programa siga funcionando

if __name__ == "__main__":
    try:
        memory_subscriber()
    except rospy.ROSInterruptException:
        pass 
