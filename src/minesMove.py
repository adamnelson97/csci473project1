#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import sys
#sys.argv[0] = script name
#sys.argv[1] = speed
#sys.argv[2] = distance
#sys.argv[3] = Forward (1)/Backward (0)

def move(spd, dis, direc):

    rospy.init_node('robot_turtle', anonymous=True)
    velo_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    
    speed = int(spd)
    distance = float(dis)
    forward = int(direc)
    

    if(forward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)

    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    
    t0 = float(rospy.Time.now().to_sec())
    current_distance = 0

    print "=======MOVE======="
    print "Speed: ", speed
    print "Distance: ", distance
    print "Fwd(1)/Bkwd(0): ", forward

    while(current_distance < distance):
        velo_pub.publish(vel_msg)
        t1=float(rospy.Time.now().to_sec())
        current_distance= speed*(t1-t0)

    vel_msg.linear.x = 0
    velo_pub.publish(vel_msg)

if __name__ == '__main__':
    print "Speed: ", sys.argv[1]
    print "Distance: ", sys.argv[2]
    print "Fwd(1)/Bkwd(0): ", sys.argv[3]

    try:
        #Testing our function
        move(sys.argv[1], sys.argv[2], sys.argv[3])
    except rospy.ROSInterruptException: pass
