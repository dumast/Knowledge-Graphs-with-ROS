import roslibpy
import roslibpy.tf

def update_position(current_pos):
    global position
    position = current_pos
    print("POSITION:")
    print(position)

client = roslibpy.Ros(host="0.0.0.0", port=9090)
client.run()

tf_client = roslibpy.tf.TFClient(client, "/2ndFloorWhole_map")
tf_client.subscribe("base_link", update_position)