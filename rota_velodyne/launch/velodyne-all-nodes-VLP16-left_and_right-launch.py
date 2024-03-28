import os
import launch
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Path to the left lidar launch file
    left_lidar_launch_file = os.path.join(get_package_share_directory('velodyne'), 'launch', 'velodyne-all-nodes-VLP16-left-launch.py')

    # Path to the right lidar launch file
    right_lidar_launch_file = os.path.join(get_package_share_directory('velodyne'), 'launch', 'velodyne-all-nodes-VLP16-launch.py')

    return launch.LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([left_lidar_launch_file]),
            launch_arguments={}.items(),
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([right_lidar_launch_file]),
            launch_arguments={}.items(),
        ),
    ])

