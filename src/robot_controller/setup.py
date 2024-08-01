from setuptools import find_packages, setup

package_name = 'robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kiran',
    maintainer_email='kiran@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'commander = robot_controller.main_control:main',
            'robot1 = robot_controller.robot1:main',
            'robot2 = robot_controller.robot2:main',
            'robot3 = robot_controller.robot3:main',
          'client_node = robot_controller.client:main',
          'service_node = robot_controller.service:main'
          ],
    },
)
