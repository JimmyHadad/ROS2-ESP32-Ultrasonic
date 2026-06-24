from setuptools import find_packages, setup

package_name = 'my_first_package'

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
    maintainer='jimmy',
    maintainer_email='jimmy@todo.todo',
    description='My first ROS 2 package for distance sensor',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # السطر الخاص بالـ Publisher اللي بيقرا من الـ ESP32
            'my_node = my_first_package.my_first_node:main',
            # السطر الجديد الخاص بالـ Subscriber اللي بياخد القرار
            'my_sub = my_first_package.my_sub_node:main'
        ],
    },
)
