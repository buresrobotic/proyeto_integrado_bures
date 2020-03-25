#!/usr/bin/env python
# license removed for brevity
import rospy #se importan los modulos necesarios
from std_msgs.msg import Int16

def callback(msg): #se crea una funcion que reciba el mensaje del publicador
    rospy.loginfo("mensaje recibido: %s",msg.data)

def ej1(): #funcion principal
    pub = rospy.Publisher('numeros3_1', Int16, queue_size=0) #creacion del publicador
    rospy.init_node('ej3_1', anonymous=True) #creacion del nodo
    while not rospy.is_shutdown():
        try:
            hello_str=int(input("Dame un numero ")) #solicita un numero por pantalla 
            pub.publish(hello_str) #se publica ese numero
            global contador #se hace global un contador
            contador=contador+1 #por cada numero que se de aumenta 1
            if contador==5: #controlador para que solo muestre un mensaje            contador=contador+1 #por cada numero que se de aumenta 1
            if contador==5: #si se llega a 5
                rospy.Subscriber('numeros3_2',Int16,callback) #se recibe la suma del publicador del 2
        except NameError:
            error="Eso no es un numero "
            rospy.loginfo(error)

if __name__ == '__main__':
    try:
        contador=0
        ej1()
    except rospy.ROSInterruptException:
        pass 