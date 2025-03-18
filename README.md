# 使用说明

1. 需要ros1和ros2。
1. 需要ros1下同名的自定义消息
1. 先转换到ros1下同名的消息，再使用工具转到ros2

# ros1同名自定义消息

在ros1下编译此仓库，`livox_interfaces`

# ros1转换消息

`livox_convert_livox2.py`文件中，看看你使用的消息是什么，就改成from什么

```
from livox_interfaces.msg import CustomMsg as LivoxCustomMsgV2, CustomPoint as LivoxCustomPointV2
from maping_msgs.msg import CustomMsg as LivoxCustomMsg
```

在当前目录运行命令

> 一定要提前source一下自定义消息的devel的setup.bash

```
python3 ./livox_convert_livox2.py xxx xxx
```

# ros1到ros2

```
rosbags-convert --src xxx --dst xxx
```

