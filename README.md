# 🤖 ROS 2 & ESP32 Ultrasonic Bridge (Sense & Think)

A real-time robotics perception system. This project bridges physical sensor data from an ESP32 microcontroller directly into the ROS 2 ecosystem, creating the foundational "Sense and Think" steps for autonomous robotics.

## 👨‍💻 Author
**Jimmy Hadad**

## 🎯 Project Objective
To design and implement a responsive obstacle detection system. By utilizing serial communication between an ESP32 and a ROS 2 node, the system translates physical distance measurements into ROS 2 topics and analyzes them in real-time to trigger safety warnings.

## ⚙️ Hardware & Software Stack
* **Microcontroller:** ESP32 Development Board
* **Sensor:** HC-SR04 Ultrasonic Sensor
* **Operating System:** Ubuntu Linux
* **Framework:** ROS 2 (Humble)
* **Languages:** Python (ROS Nodes) & C++ (ESP32 Firmware)

## 🚀 Key Features
* **Real-Time Serial Bridge:** A custom ROS 2 Publisher node that reads serial data from the ESP32 and broadcasts it to the `/sonar_distance` topic instantly.
* **Intelligent Brain (Subscriber):** A processing node that listens to distance data and makes real-time decisions based on a critical safety threshold (15 cm). It prints "Safe Zone" messages or triggers an immediate "WARNING" when an obstacle is too close.

## 🎬 Live Demonstration
![Hardware Setup](https://github.com/user-attachments/assets/38342813-ef33-4272-83fc-ec11fa85c5fb)

[https://github.com/user-attachments/assets/b7eed5ec-dba1-4d6d-ae1c-3cf0160db50a](https://github.com/user-attachments/assets/b7eed5ec-dba1-4d6d-ae1c-3cf0160db50a)

## 💻 ESP32 C++ Firmware Logic
The ESP32 is programmed using standard C++ via the Arduino IDE. Its primary role is to trigger the HC-SR04 ultrasonic sensor, measure the echo pulse duration, and calculate the physical distance in centimeters. This numerical data is then continuously streamed over the Serial port (baud rate 115200), serving as the raw, real-time data feed for the ROS 2 Bridge node to pick up.

## 📂 Repository Structure
* `my_first_package/` : The main ROS 2 Python package directory containing the source code.
* `my_first_node.py` : The Publisher node acting as the serial bridge for the ESP32.
* `my_sub_node.py` : The Subscriber node containing the decision-making and warning logic.
* `setup.py` : Configuration file for building the ROS 2 package.
* `esp32_ultrasonic.ino` : The C++ firmware file for the ESP32 microcontroller.

## ⚠️ Setup & Deployment

1. **Hardware Setup (C++):** Connect the HC-SR04 to the ESP32 and upload the C++ firmware using the Arduino IDE.

2. **Serial Permissions:** Plug the ESP32 into your Ubuntu machine and grant read/write access to the serial port:

        sudo chmod 666 /dev/ttyACM0

3. **Build the Workspace:** Navigate to your `ros2_ws` and compile the package:

        colcon build --packages-select my_first_package
        source install/setup.bash

4. **Run the System:** * **Terminal 1 (The Bridge):** `ros2 run my_first_package my_node`
    * **Terminal 2 (The Brain):** `ros2 run my_first_package my_sub`
