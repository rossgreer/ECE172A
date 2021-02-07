'''
ECE 172A, Homework 2 Robot Kinematics
Author: regreer@ucsd.edu
For use by UCSD ECE 172A students only.
'''

import numpy as np
import matplotlib.pyplot as plt

def forwardKinematics(theta0, theta1, theta2, l0, l1, l2):
	return 0

def inverseKinematics(l0,l1,l2,x_e_target,y_e_target):
	'''
	This function is supposed to implement inverse kinematics for a robot arm
	with 3 links constrained to move in 2-D. The comments will walk you through
	the algorithm for the Jacobian Method for inverse kinematics.

	INPUTS:
	l0, l1, l2: lengths of the robot links
	x_e_target, y_e_target: Desired final position of the end effector 

	OUTPUTS:
	theta0_target, theta1_target, theta2_target: Joint angles of the robot that
	take the end effector to [x_e_target,y_e_target]
	'''

    # Initialize for the plots:
    end_effector_positions = []

    # Initialize the thetas to some value
    
    # Obtain end effector position x_e, y_e for current thetas: 
    # HINT: use your ForwardKinematics function   
    
    
    while 1: # Replace the '1' with a condition that checks if your estimated [x_e,y_e] is close to [x_e_target,y_e_target]
        
        # Calculate the Jacobian matrix for current values of theta
        # HINT: write a function for doing this      
        
        
        # Calculate the pseudo-inverse of the jacobian (HINT: numpy pinv())     
        

        # Update the values of the thetas by a small step


        # Obtain end effector position x_e, y_e for the updated thetas:
    
        
        # If you would like to visualize the iterations, draw the robot using drawRobot. 

        
        # Save end effector positions for the plot:
    

    # Plot the final robot pose


    # Plot the end effector position through the iterations


    return 0
    

def drawRobot(x_1,y_1,x_2,y_2,x_e,y_e):
	x_0, y_0 = 0, 0
	plt.plot([x_0, x_1, x_2, x_e], [y_0, y_1, y_2, y_e], lw=4.5)
	plt.scatter([x_0, x_1, x_2, x_e], [y_0, y_1, y_2, y_e], color='r')
	plt.show()

