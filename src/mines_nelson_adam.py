#!/usr/bin/env python
from minesMove import move
from minesRotate import rotate
import rospy

if __name__ == '__main__':
    rx = 40
    sx = 20
    try:
	#1
        rotate(rx, 60, 0)
        move(sx, 2, 1)
	#2
	rotate(rx, 140, 1)
	move(sx, 2, 1)
	#3
	rotate(rx, 90, 1)
	move(sx, 0.5, 1)
	#4
	rotate(rx, 90, 0)
	move(sx, 0.7, 1)
	#5
	rotate(rx, 90, 0)
	move(sx, 2, 1)
	#6
	rotate(rx, 90, 0)
	move(sx, 0.7, 1)
	#6.5
	rotate(rx, 90, 0)
	move(sx, 0.5, 1)
	#7
	rotate(rx, 90, 1)
	move(sx, 2.5, 1)
	#8
	rotate(rx, 90, 1)
	move(sx, 0.5, 1)
	#9
	rotate(rx, 90, 0)
	move(sx, 0.7, 1)
	#10
	rotate(rx, 90, 0)
	move(sx, 1.9, 1)
	#11
	rotate(rx, 60, 0)
	move(sx, 1.9, 1)
	#12
	rotate(rx, 120, 1)
	move(sx, 1.9, 1)
	#13
	rotate(rx, 60, 0)
	move(sx, 1.9, 1)
	#14
	rotate(rx, 90, 0)
	move(sx, 0.7, 1)
	#15
	rotate(rx, 90, 0)
	move(sx, 0.5, 1)
	#16
	rotate(rx, 90, 1)
	move(sx, 2.5, 1)
	#17
	rotate(rx, 90, 1)
	move(sx, 0.5, 1)
	#18
	rotate(rx, 90, 0)
	move(sx, 0.5, 1)
	#19
	rotate(rx, 90, 0)
	move(sx, 2, 1)
	#20
	rotate(rx, 90, 0)
	move(sx, 0.7, 1)
	#21
	rotate(rx, 90, 0)
	move(sx, 0.5, 1)
	#22
	rotate(rx, 90, 1)
	move(sx, 2.2, 1)
	#23
	rotate(rx, 140, 1)
	move(sx, 2, 1)
    except rospy.ROSInterruptException:
        pass
