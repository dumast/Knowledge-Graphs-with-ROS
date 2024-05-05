import roslibpy
import roslibpy.tf.TFClient

def update_position(current_pos):
    global position
    position = current_pos
    print("POSITION:")
    print(position)

tf_client = roslibpy.tf.TFClient(client, "/2ndFloorWhole_map")
tf_client.subscribe("base_link", update_position)