#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI = 3.14159265358979323846
import sys
#sys.argv[0] = script name
#sys.argv[1] = speed
#sys.argv[2] = angle
#sys.argv[3] = Clockwise (1)/Counter-Clockwise (0)

def rotate(spd, ang, clckws):

    rospy.init_node('robot_turtle', anonymous=True)
    velo_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    speed = int(spd)
    angle = int(ang)
    clockwise = int(clckws)

    angular_speed = speed*2*PI/360
    relative_angle = angle*2*PI/360

    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)

    t0 = float(rospy.Time.now().to_sec())
    current_angle = 0

    print "======ROTATE======"
    print "Speed: ", speed
    print "Angle(Deg): ", angle
    print "CW(1)/CCW(0): ", clockwise

    while(current_angle <= relative_angle):
        velo_pub.publish(vel_msg)
        t1=float(rospy.Time.now().to_sec())
        current_angle = angular_speed*(t1-t0)

    vel_msg.angular.z = 0
    velo_pub.publish(vel_msg)
    #sys.exit()

if __name__ == '__main__':
    print "Speed: ", sys.argv[1]
    print "Angle(Deg): ", sys.argv[2]
    print "CW(1)/CCW(0): ", sys.argv[3]

    try:
        rotate(sys.argv[1], sys.argv[2], sys.argv[3])
    except rospy.ROSInterruptException:
        pass
