#!/usr/bin/env python
# license removed for brevity
import rospy #se importan los modulos necesarios
from std_msgs.msg import Int16

def callback(msg): #se define una funcion que reciba el mensaje del publicador del 1
    lista.append(int(msg.data)) #incluye el numero en la lista
    rospy.loginfo("mensaje recibido: %s",msg.data) #muestra el numero recibido por pantalla
    if len(lista)==10: #si la longitud de la lista es 10
        pub.publish(sum(lista)) #se publica su suma
        del(lista[0:]) #y se deja la lista sin elementos

def memory_subscriber(): #funcion principal
    rospy.init_node('suscriptor_ej2',anonymous=True) #se crea el nodo
    global pub  #se hace global el publiador
    pub = rospy.Publisher('numeros3_2', Int16, queue_size=0)  #se crea el publicador
    rospy.Subscriber('numeros3_1',Int16,callback) #y el suscriptor
    rospy.spin()

if __name__ == "__main__":
    try:
        lista=[]
        memory_subscriber() #se llama a la funcion principal
    except rospy.ROSInterruptException:
        pass 
