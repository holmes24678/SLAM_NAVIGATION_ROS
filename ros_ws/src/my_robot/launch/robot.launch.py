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
    world_file = os.path.join(get_package_share_path('my_robot'),
                              'world','my_world.world')
     #urdf file
    urdf_file = os.path.join(get_package_share_path('my_robot'),'urdf','my_robot.urdf.xacro')

    #robot description
    robot_description = ParameterValue(Command(['xacro ', urdf_file]),value_type=str)

    #directory of rviz config file
    rviz_config_dir = os.path.join(get_package_share_path('my_robot'),'rviz','my_robot_config.rviz')
    
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