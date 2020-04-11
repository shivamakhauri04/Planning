#!/usr/bin/env python
import Astar_rigid
import rospy
import numpy as np
from geometry_msgs.msg import Twist
from time import sleep
import math
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import sys



class GoForward():
    def __init__(self,action,myargv):
        self.act = action
        self.yaw = 0
        self.myargv = myargv
        # initiliaze
        
        rospy.init_node('roombaRobot', anonymous=True,log_level=rospy.WARN)
	# tell user how to stop TurtleBot
	rospy.loginfo("To stop TurtleBot CTRL + C")
        # What function to call when you ctrl + c    
        rospy.on_shutdown(self.shutdown)
        self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
        #self.odom = rospy.Subscriber('/odom',Odometry,callback)
	sub = rospy.Subscriber ('/odom', Odometry, self.get_rotation)
        r = rospy.Rate(1);
        index = 0

        
        sleep(10)
        step = [int(myargv[5]),int(myargv[6])]
        
	# as long as you haven't ctrl + c keeping doing...
        while not rospy.is_shutdown():
                print ("here") 
                #print (self.act)            
                for act in self.act[1:]:
                        if (abs(act[1]-act[0])==60):
                                radius = 0.038
                                L = 0.354
                                move_cmd = Twist()
                                
                                print ((float(radius/L))*(act[1]-act[0]))
                        
                                move_cmd.linear.x = (float(radius/2))*(act[0]+act[1])*0.35  #0.35
                                move_cmd.angular.z = (float(radius/L))*(act[1]-act[0]) *0.35 #35
                        
                                self.cmd_vel.publish(move_cmd)
                                # wait for 0.1 seconds (10 HZ) and publish again
                                sleep(1)
                        
                        elif (abs(act[1]-act[0])==30 and (act[0]== 60 or act[1]==60)):
                                radius = 0.038
                                L = 0.354
                                move_cmd = Twist()
                                
                                print ((float(radius/L))*(act[1]-act[0]))
                        
                                move_cmd.linear.x = (float(radius/2))*(act[0]+act[1]) * 1.05 #1.05  
                                move_cmd.angular.z = (float(radius/L))*(act[1]-act[0]) * 1.07 # 1.07
                        
                                self.cmd_vel.publish(move_cmd)
                                # wait for 0.1 seconds (10 HZ) and publish again
                                sleep(1)

                        elif (abs(act[1]-act[0])==30 and (act[0]!= 60 and act[1]!=60)):
                                index = index +1
                                radius = 0.038
                                L = 0.354
                                move_cmd = Twist()
                                
                                print ((float(radius/L))*(act[1]-act[0]))
                        
                                move_cmd.linear.x = (float(radius/2))*(act[0]+act[1]) *0.8 #0.95
                                move_cmd.angular.z = (float(radius/L))*(act[1]-act[0]) * 1.09 # 1.1
                        
                                self.cmd_vel.publish(move_cmd)
                                # wait for 0.1 seconds (10 HZ) and publish again
                                sleep(1)

                                if index == 4 and int(self.myargv[3])==4  and int(self.myargv[4])==4:
                                        move_cmd.angular.z = 5 # 1.1
                                        self.cmd_vel.publish(move_cmd)
                                        sleep(1)

                        else :
                                for _ in range (38):
                                        radius = 0.038
                                        L = 0.354
                                        move_cmd = Twist()
                                        print ((float(radius/2))*(act[0]+act[1]) )
                                        print (float(radius/L))*(act[1]-act[0])
                                        move_cmd.linear.x = (float(radius/2))*(step[0]+step[1])*0.28 #0.19
                                        move_cmd.angular.z = (float(radius/L))*(act[1]-act[0]) 
                                        self.cmd_vel.publish(move_cmd)
                                        sleep(0.1)

                command = Twist()
                command.linear.x = 0
                command.angular.z = 0
                cmd_publish.publish(command)
                
    def get_rotation (self,msg):
        orientation_q = msg.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (roll, pitch, self.yaw) = euler_from_quaternion (orientation_list)
        
    def shutdown(self):
        # stop turtlebot
        rospy.loginfo("Stop TurtleBot")
	# a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
        self.cmd_vel.publish(Twist())
	# sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
        rospy.sleep(10)
 
if __name__ == '__main__':
    try:
	myargv = rospy.myargv(argv=sys.argv)
        act = Astar_rigid.main(myargv)
        print (act)
        
        GoForward(act,myargv)
    except:
        rospy.loginfo("GoForward node terminated.")

