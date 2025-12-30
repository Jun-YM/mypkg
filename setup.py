from setuptools import find_packages, setup

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/wifi_monitor.launch.py']),
    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jun0606',
    maintainer_email='s24C1133la@s.chibakoudai.jp',
    description='ロボットシステム学授業用',
    license='BSD－3－Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
             'wifi_signal_publisher = mypkg.wifi_signal_publisher:main', #talker.pyのmain関数という意味
            'wifi_alert_node = mypkg.wifi_alert_node:main',
        ],
    },
)
