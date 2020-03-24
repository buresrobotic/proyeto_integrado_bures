#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int16

def callback(msg):
    lista.append(int(msg.data))
    rospy.loginfo("mensaje recibido: %s",msg.data)
    if len(lista)==5:
        pub.publish(sum(lista))
        #rospy.loginfo(sum(lista))
        del(lista[0:])

def memory_subscriber():
    rospy.init_node('suscriptor_ej2',anonymous=True)
 #el primer argumento, es el nombrel del topic al que queremos suscribirnos...
 #el segundo argumento es el tipo de mensaje,
    global pub  
    pub = rospy.Publisher('numeros3_2', Int16, queue_size=0)
    rospy.Subscriber('numeros3_1',Int16,callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        lista=[]
        memory_subscriber()
    except rospy.ROSInterruptException:
        pass 
