# SPDX-FileCopyrightText: 2025 Junpei Yamamoto
# SPDX-License-Identifier: BSD-3-Clause

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mypkg',
            executable='wifi_signal_publisher',
            name='wifi_signal_publisher',
            output='screen'
            emulate_tty=True
        ),
        Node(
            package='mypkg',
            executable='wifi_alert_node',
            name='wifi_alert_node',
            parameters=[{'threshold': -70}],
            output='screen'
            emulate_tty=True
        )
    ])

