#!/usr/bin/env python3.9
# license removed for brevity

import rospy

import sys
import streamlit.web import cli as stcli

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        
        sys.argv = ['streamlit', 'run', 'retrieve.py']
        sys.exit(stcli.main())
        
        # result = movebase_client(target_x, target_y)
        # if result:
        #     rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")