# KUKA IIWA 14 - Lower Limb Rehabilitation

This code is developed for the published research paper [Novel method for lower limb rehabilitation based on brain-computer interface and transcutaneous spinal cord electrical stimulation](https://ieeexplore.ieee.org/abstract/document/9912550).


This package uses KUKA-IIWA-ROS-API (https://github.com/jonaitken/KUKA-IIWA-API) for communicating with kuka sunrise to control the robot.  



- connect ethernet connection from kuka Sunrise
- set ethernet config:
    - ip: 172.31.1.50
    - Netmask: 255.255.255.0
    - Gateway: 255.255.255.0
- clone the repository
- run `roscore` in terminal
- run `python3 server_V30032017.py`
- run `python3 main.py`
