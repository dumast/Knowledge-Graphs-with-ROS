#!/usr/bin/env python3.9

# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

import tf2_ros

import rospy

def movebase_client(target_x, target_y):

   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()
    
    tf_buffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tf_buffer)
    
    
    trans = tf_buffer.lookup_transform('base_link','odom',rospy.Time(0))
    
    x = trans.transform.translation.x
    y = trans.transform.translation.y
    
    print(f"ROBOT_X: {x}")
    print(f"ROBOT_Y: {y}")
    
    print(f"GOAL_X: {target_x - x}")
    print(f"GOAL_X: {target_y - y}")
    
    

   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "base_link"
    goal.target_pose.header.stamp = rospy.Time.now() 
   # Move 0.5 meters forward along the x axis of the "map" coordinate frame 
    goal.target_pose.pose.position.x = target_x - x
    goal.target_pose.pose.position.y = target_y - y
   # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.w = 1.0

   # Sends the goal to the action server.
    client.send_goal(goal)
   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()
   # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
    # Result of executing the action
        return client.get_result()   