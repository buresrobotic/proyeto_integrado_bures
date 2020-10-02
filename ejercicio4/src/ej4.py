#!/usr/bin/env python

import rospy
from ejercicio4.msg import datos

rospy.init_node("publicador_datos")
pub=rospy.Publisher("mensaje",datos,queue_size=1)
rate=rospy.Rate(2)
mis_datos=datos()
mis_datos.edad=19
mis_datos.nombre="bures"
mis_datos.coeficiente=2.6
while not rospy.is_shutdown():
    pub.publish(mis_datos)
    rate.sleep()