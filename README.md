
## Project Setup 
Make sure that you are using Linux Distribution in my case i am using Ubuntu Jazzy. The Distribution of ROS is humble
## Installation and Setup ROS
https://docs.ros.org/en/humble/Installation/Alternatives/Ubuntu-Development-Setup.html
## after Successful Installation of ROS install colcon

```javascript
sudo apt install python3-colcon-common-extensions
```
## Create ROS workspace
```javascript
mkdir -p ros2_ws/src 
cd ros2_ws
```
## change directory to src create ROS package
```javascript
ros2 pkg create my_robot --build-type ament_python
```
## you will get output as 
```javascript
going to create a new package
package name: my_robot
destination directory: /home/sherlock/Desktop/ros2
package format: 3
version: 0.0.0
description: TODO: Package description
maintainer: ['sherlock <sherlock@todo.todo>']
licenses: ['TODO: License declaration']
build type: ament_python
dependencies: []
creating folder ./my_robot
creating ./my_robot/package.xml
creating source folder
creating folder ./my_robot/my_robot
creating ./my_robot/setup.py
creating ./my_robot/setup.cfg
creating folder ./my_robot/resource
creating ./my_robot/resource/my_robot
creating ./my_robot/my_robot/__init__.py
creating folder ./my_robot/test
creating ./my_robot/test/test_copyright.py
creating ./my_robot/test/test_flake8.py
creating ./my_robot/test/test_pep257.py

[WARNING]: Unknown license 'TODO: License declaration'.  This has been set in the package.xml, but no LICENSE file has been created.
It is recommended to use one of the ament license identitifers:
Apache-2.0
BSL-1.0
BSD-2.0
BSD-2-Clause
BSD-3-Clause
GPL-3.0-only
LGPL-3.0-only
MIT
MIT-0
```
## build the package using colcon
```javascript
colcon build --symlink-install
```
## open .bashrc and add 
```javascript
gedit ~/.bashrc

source ~/ros_ws/install/setup.bash <this will be the path of your node setup.bash change it according to you>
```
## you will get output as 
```javascript
Starting >>> my_robot
Finished <<< my_robot [1.85s]          

Summary: 1 package finished [2.27s]

```
## Now let's install Visual Studio Code
```javascript
sudo apt get install code-classic

```
## open VS code
```javascript
code .
```
## open my_robot folder delete include and src folders and create a folder as urdf then, open and  change the CmakeList.txt as
```javascript
cmake_minimum_required(VERSION 3.8)
project(my_robot)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
install(
  DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME}/
)


ament_package()

```
### Change directory to urdf and create xacro files
```javascript
touch common_properties.xacro data.xacro my_robot.urdf.xacro
```
common_properties.xacro will gives the common_properties of elements of the my_robot,
data.xacro contains the information related to links and joints of my_robot,
my_robot.urdf.xacro is the urdf file which will gives the my_robot 
### go to ros2_ws directory and run
```javascript
colcon build --symlink-all
```
you will get 
```javascript
Starting >>> my_robot
Finished <<< my_robot [0.72s]                  

Summary: 1 package finished [1.12s]
```
then
```javacript
ros2 run robot_state_publisher robot_state_publisher  --ros-args -p robot_description:="$(xacro my_robot.urdf.xacro)"
```
robot_state_publisher is a node which will publish the URDF data of the model throgh robot_description topic

you will get
```javascript
[INFO] [1716620285.821425522] [robot_state_publisher]: got segment base_footprint
[INFO] [1716620285.821547375] [robot_state_publisher]: got segment base_link
[INFO] [1716620285.821576289] [robot_state_publisher]: got segment first_wheel
[INFO] [1716620285.821602717] [robot_state_publisher]: got segment second_wheel
[INFO] [1716620285.821628170] [robot_state_publisher]: got segment sphere

```
your UDRF is being published over robot_description topic
### we need to visualize what it is publishing for that we use tool called 'RVIZ'
on your terminal
```javascript
ros2 run rviz2 rviz2
```
### you will get output as 

![Screenshot from 2024-05-25 12-37-10](https://github.com/holmes24678/SLAM_AND_NAVIGATION_USING_ROS/assets/42709209/95232e76-4272-43f6-9796-89e92ca08c20)

You Successfully completed loading your robot
### Next step is to launch the file in gazebo 
gazebo is a open source simulator

### Lets install gazebo 
```javascript
sudo apt install ros-humble-gazebo*
```
open /.bashrc and add this at the end of license
```javascript
source /usr/share/gazebo/setup.bash

```
### Now Lets check by running on your terminal
```javascript
gazebo
```
You will get 

![Screenshot from 2024-05-25 13-00-42](https://github.com/holmes24678/SLAM_AND_NAVIGATION_USING_ROS/assets/42709209/5fc6c1e9-fb63-464f-b225-5e311840c9d0)

you have Successfully installed gazebo then lets spawn our model in gazebo

```javascript
ros2 run robot_state_publisher robot_state_publisher  --ros-args -p robot_description:="$(xacro my_robot.urdf.xacro)"
```
this will publish urdf model on robot_description topic
```javascript
ros2 run gazebo_ros spawn_entity.py -topic robot_description -entity my_robot

```
this will spawn the robot using robot_description topic
### Then you will get output 
```javacript
[INFO] [1716623056.227692726] [spawn_entity]: Spawn Entity started
[INFO] [1716623056.228185963] [spawn_entity]: Loading entity published on topic robot_description
/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/qos.py:307: UserWarning: DurabilityPolicy.RMW_QOS_POLICY_DURABILITY_TRANSIENT_LOCAL is deprecated. Use DurabilityPolicy.TRANSIENT_LOCAL instead.
  warnings.warn(
[INFO] [1716623056.235275071] [spawn_entity]: Waiting for entity xml on robot_description
[INFO] [1716623056.238057233] [spawn_entity]: Waiting for service /spawn_entity, timeout = 30
[INFO] [1716623056.238857809] [spawn_entity]: Waiting for service /spawn_entity
[INFO] [1716623056.256798649] [spawn_entity]: Calling service /spawn_entity
[INFO] [1716623056.503763710] [spawn_entity]: Spawn status: SpawnEntity: Successfully spawned entity [my_robot]

```
You Successfully spawned the your robot
### Lets visualize it in gazebo using gazebo.launch.py
```javascript
ros2 run gazebo_ros gazebo.launch.py
```
### You will get

![Screenshot from 2024-05-25 13-20-30](https://github.com/holmes24678/SLAM_AND_NAVIGATION_USING_ROS/assets/42709209/153aea76-c3c8-4ba6-99dd-6e0a693c4275)

you have Successfully launched your robot in gazebo.

### Now lets try to create a world inside the Gazebo 

open Gazebo using command line 

Then Edit -> Building Editor : Build your custom world and save it then Save this as world ( in my case world file name : my_world.world)

### Now Lets launch this world in Gazebo 
```javascript
ros2 launch gazebo_ros gazebo.launch.py world:=./my_robot/world/my_world.world
```
You will get

![Screenshot from 2024-05-25 23-59-30](https://github.com/holmes24678/SLAM_AND_NAVIGATION_USING_ROS/assets/42709209/59058429-b2d2-4381-9a26-c7b6351fb666)

You have Successfully launched your world in Gazebo

### Launch both robot model and world in Gazebo 
```javascript
ros2 run robot_state_publisher robot_state_publisher  --ros-args -p robot_description:="$(xacro my_robot.urdf.xacro)"

ros2 launch gazebo_ros gazebo.launch.py world:=./my_robot/world/my_world.world

ros2 run gazebo_ros spawn_entity.py -topic robot_description -entity my_robot

ros2 run rviz2 rviz2

```
On Rviz save the configuration so that we dont need to add display type we can directly use this configuration as rviz argument

## Lets add Sensor to the Model

Add new file to URDF as laser.xacro and include it in the my_robot.urdf.xacro and add gazebo plugin as shown below

```javascript
   <!-- hokuyo -->
  <gazebo reference="ray_link">
    <material>
      Gazebo/Red
    </material>
    <sensor type="ray" name="laser">
      <pose>0 0 0 0 0 0</pose>
      <visualize>true</visualize>
      <update_rate>10</update_rate>
      <ray>
        <scan>
          <horizontal>
            <samples>360</samples>
            <resolution>1</resolution>
            <min_angle>-3.14</min_angle>
            <max_angle>3.14</max_angle>
          </horizontal>
        </scan>
        <range>
          <min>0.30</min>
          <max>10.0</max>
          <resolution>0.01</resolution>
        </range>
  
      </ray>
      <plugin name="laser_controller" filename="libgazebo_ros_ray_sensor.so">
        <ros>
          <argument>~/out:=scan</argument>
        </ros>
        <output_type>sensor_msgs/LaserScan</output_type>
        <frame_name>ray_link</frame_name>
      </plugin>
    </sensor>
  </gazebo>
```

after running REQUIRED commands

You will get 

![Screenshot from 2024-05-26 00-19-55](https://github.com/holmes24678/SLAM_AND_NAVIGATION_USING_ROS/assets/42709209/e50375c8-832f-4b9e-bf06-eb25a9fd4ab1)

you have Successfully added Laser link and plugin

## Now its time to Control the model in Gazebo 

For Controlling we have plugin called  'diff_drive_control'

after addding it to run the following command to control by keyboard

```javascript
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
You will get 
```javascript
This node takes keypresses from the keyboard and publishes them
as Twist/TwistStamped messages. It works best with a US keyboard layout.
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

For Holonomic mode (strafing), hold down the shift key:
---------------------------
   U    I    O
   J    K    L
   M    <    >

t : up (+z)
b : down (-z)

anything else : stop

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%

CTRL-C to quit

currently:	speed 0.5	turn 1.0 
```

Now you will able to control the robot in gazebo

## Create a launch file to run all nodes at once

Launch file is type of file where you can launch multipe nodes at onces by writing a launch file

Create a folder launch and create file robot.launch.py

```javascript
import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from ament_index_python.packages import get_package_share_path
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    #world file
    world_file = os.path.join(get_package_share_path('my_robot_bringup'),
                              'worlds','world.world')
     #urdf file
    urdf_file = os.path.join(get_package_share_path('my_robot_description'),'urdf','my_robot.urdf.xacro')

    #robot description
    robot_description = ParameterValue(Command(['xacro ', urdf_file]),value_type=str)

    #directory of rviz config file
    rviz_config_dir = os.path.join(get_package_share_path('my_robot_bringup'),'rviz','my_robot_config.rviz')

    #twist mux params
    twist_mux_params = os.path.join(get_package_share_path('my_robot_description'),'config','twist_mux.yaml')
    
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description' : robot_description}]
    )

    #including gazebo launch description
    launch_include = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch','gazebo.launch.py')),
            launch_arguments = {'world':world_file}.items()
    )

    #spawning in gazebo
    gazebo_node = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments= ['-entity', 'my_robot',
                    '-topic', 'robot_description'],
        output = 'screen'
    )

    #launching in RVIZ
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        output = "screen",
        arguments=['-d', rviz_config_dir]
    )

    return LaunchDescription([
        launch_include,
        robot_state_publisher,
        rviz_node,
        gazebo_node
    ])
```
Make changes to CmakeList.txt

```javascript
cmake_minimum_required(VERSION 3.8)
project(my_robot)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
install(
  DIRECTORY urdf world rviz launch
  DESTINATION share/${PROJECT_NAME}/
)


ament_package()

```
use colcon build to make changes

```javascript
colcon build --symlink-install
```
After build run the following command

```javascript
ros2 launch my_robot robot.launch.py
```
You will see every thing is opened

## Next step is to map the world by Controlling the robot throgh the world

Due to some issues with Fast DDS and Navigation in ROS2, it has been recommended to use Cyclone DDS instead. So, we need to tell ROS2 to use a different DDS.

```javascript
$ sudo apt install ros-humble-rmw-cyclonedds-cpp
```
To do this, you just need to export one environment variable named “RMW_IMPLEMENTATION”, that we will add into your .bashrc.

```javascript

export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
source /opt/ros/humble/setup.bash
```
### Now lets install slam-tool-box
```javascript
$ sudo apt install ros-humble-slam-toolbox
```
now copy cof file to your node by creating a new folder config

```javascript
cp /opt/ros/humble/share/slam_toolbox/config/mapper_params_online_async.yaml /ros_ws/src/my_robot/config/
```
after copying on ROS parameters make sure that you have set your mode to mapping
```javascript
  # ROS Parameters
    odom_frame: odom
    map_frame: map
    base_frame: base_footprint
    scan_topic: /scan
    use_map_saver: true
    mode: mapping
```
### Then run the following commands in terminal
```javascript
ros2 launch my_robot robot.launch.py

ros2 launch my_robt online_async_launch.py slam_params_file:=./src/my_robot/config/mapper_params_online_async.yaml use_sim_time:=true
```
on Rviz Add map under display type then select map topic and add LaserScan select scan topic
### You will get

![Screenshot from 2024-05-26 01-29-32](https://github.com/holmes24678/SLAM_AND_NAVIGATION_USING_ROS/assets/42709209/79cf2fc4-27b5-4db4-b417-625937dce24e)

-> Now run teleop_twist_keyboard to drvie through world

-> On RVIZ go to Panel -> add new panel -> select slam_toolbox plugin

-> Save the map and Serialize the map

-> Now you have Successfully Mapped the world using slam-toolbox

## Next step is to install Nav2 Stack For Navigation

```javascript
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup
```
After Successful Installation 

``` javascript
cp /opt/ros/humble/share/nav2_bringup/launch/localization_launch.py ros_ws/src/my_robot/launch/

cp /opt/ros/humble/share/nav2_bringup/launch/navigation_launch.py ros_ws/src/my_robot/launch/

cp /opt/ros/humble/share/nav2_bringup/params/nav2_params.yaml ros_ws/src/my_robot/config/
```
On localization_launch.py and navigation_launch.py change bringup_dir
```javascript
bringup_dir = get_package_share_directory('my_robot')
```
Build it to make the changes

## Launch saved map using using localization_launch.py
```javascript
ros2 launch my_robot localization_launch.py map:=saver.yaml use_sim_time:=true
```
this will load the saved file in RVIZ and change topic to global cost map 

## Next is to launch the navigation_launch.py to navigate the robot autonomously

```javascript
ros2 launch my_robot_bringup navigation_launch.py use_sim_time:=true map_subscribe_transient_local:=true

```
On RVIZ click on 2D post estimate to set the intial pose and 2D goal Pose to set the Goal Point

# If you did not get any error hooray!!!! you have Successfully simulated SLAM and Navigation in Gazebo using ROS


