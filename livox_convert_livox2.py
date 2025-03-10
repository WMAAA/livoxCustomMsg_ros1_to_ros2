#!/usr/bin/env python

import rosbag
import rospy
import sys
from livox_interfaces.msg import CustomMsg as LivoxCustomMsgV2, CustomPoint as LivoxCustomPointV2
from maping_msgs.msg import CustomMsg as LivoxCustomMsg

def convert_rosbag(input_bag, output_bag):
    with rosbag.Bag(input_bag, 'r') as in_bag, rosbag.Bag(output_bag, 'w') as out_bag:
        for topic, msg, t in in_bag.read_messages():
            rospy.loginfo(f"Processing topic {topic}, message type: {type(msg)}")
            
            if topic in ['/livox/imu_3JEDK6E00191551', '/livox/lidar_3JEDK6E00191551']:
                new_topic = '/livox/imu' if 'imu' in topic else '/livox/lidar'
                
                if new_topic == '/livox/lidar':
                    new_msg = LivoxCustomMsgV2()
                    new_msg.header.stamp = msg.header.stamp
                    new_msg.header.frame_id = msg.header.frame_id
                    new_msg.timebase = msg.timebase
                    new_msg.point_num = msg.point_num
                    new_msg.lidar_id = msg.lidar_id
                    new_msg.rsvd = msg.rsvd
                    new_msg.points = [
                        LivoxCustomPointV2(
                            offset_time=p.offset_time, x=p.x, y=p.y, z=p.z,
                            reflectivity=p.reflectivity, tag=p.tag, line=p.line
                        ) for p in msg.points
                    ]
                    out_bag.write(new_topic, new_msg, t)
                else:
                    out_bag.write(new_topic, msg, t)
                
                rospy.loginfo(f"Message written to {new_topic}")
            else:
                out_bag.write(topic, msg, t)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_bag> <output_bag>")
        sys.exit(1)
    
    input_bag = sys.argv[1]
    output_bag = sys.argv[2]
    
    rospy.init_node('rosbag_converter')
    convert_rosbag(input_bag, output_bag)
    rospy.loginfo("Rosbag conversion completed!")

