import roslibpy
import roslibpy.actionlib

client = roslibpy.Ros(host="0.0.0.0", port=9090)
client.run()
print("Is ROS connected?", client.is_connected)


action_client = roslibpy.actionlib.ActionClient(client, "/move_base", "move_base_msgs/MoveBaseAction")

def destination_reached(r):
    print("I did it")
    print(r)
    

def movebase_client(target_x, target_y):
    
    global move_goal

    print("going to position " + str(target_x) + ", " + str(target_y))
    message = {
        "target_pose": {
            "header": {"frame_id": "map"},
            "pose": {
                "position": {"x": target_x, "y": target_y, "z": 0.0},
                "orientation": {"x": 0.0, "y": 0.0, "z": 0, "w": 1.0},
            },
        }
    }

    move_goal = roslibpy.actionlib.Goal(action_client, message)
    move_goal.send(result_callback=destination_reached)

def cancel_goal():
    global move_goal
    if move_goal is not None:
        print("move goal cancelled")
        move_goal.cancel()
        move_goal = None