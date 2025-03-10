cmake_minimum_required(VERSION 3.0.2)
project(livox_interfaces)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  std_msgs
)

# 声明消息文件
add_message_files(
  FILES
  CustomMsg.msg
  CustomPoint.msg
)

# 生成消息
generate_messages(
  DEPENDENCIES
  std_msgs
)

# 声明 catkin 依赖
catkin_package(
  CATKIN_DEPENDS message_runtime std_msgs
)

# 包含头文件路径
include_directories(
  ${catkin_INCLUDE_DIRS}
)

