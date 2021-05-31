#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

class MoveTurtle:

    def __init__(self):
        # Starts a new node
        #rospy.init_node('moveturtle', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.vel_msg = Twist()
        self.linearSpeed = 0.1
        self.angularSpeed = 0.5

    def Up(self):
        self.vel_msg.linear.x= 1.5
        self.vel_msg.linear.y= 0.0
        self.vel_msg.linear.z= 0.0
        self.vel_msg.angular.x= 0
        self.vel_msg.angular.y= 0
        self.vel_msg.angular.z= 0
        self.velocity_publisher.publish(self.vel_msg)

    def Down(self):
        self.vel_msg.linear.x=-1.5
        self.vel_msg.linear.y= 0.0
        self.vel_msg.linear.z= 0.0
        self.vel_msg.angular.x= 0
        self.vel_msg.angular.y= 0
        self.vel_msg.angular.z= 0
        self.velocity_publisher.publish(self.vel_msg)

    def Left(self):
        self.vel_msg.linear.x= 0.0
        self.vel_msg.linear.y= 0.0
        self.vel_msg.linear.z= 0.0
        self.vel_msg.angular.x= 0
        self.vel_msg.angular.y= 0
        self.vel_msg.angular.z= 1.55
        self.velocity_publisher.publish(self.vel_msg)

    def Right(self):
        self.vel_msg.linear.x= 0.0
        self.vel_msg.linear.y= 0.0
        self.vel_msg.linear.z= 0.0
        self.vel_msg.angular.x= 0
        self.vel_msg.angular.y= 0
        self.vel_msg.angular.z=-1.55
        self.velocity_publisher.publish(self.vel_msg)