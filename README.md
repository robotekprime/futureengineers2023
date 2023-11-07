
***

**Official repository of the Robotek Prime team from Kazakhstan. It contains all the engineering materials of our self-driven vehicle's model participating in the WRO Future Engineers competition in the season of 2023.**

***

<div align=center>

![logo](./img/banner2.png)

</div>

***

## Contents

* [**Mobility Management**](#mobility-management)
  * [Motor Selection and Implementation](#motor-selection-and-implementation)
  * [Chassis Design and Implementation](#chassis-design-and-implementation)
* [**Power and Sense Management**](#power-and-sense-management)
  * [Sensor Management](#sensor-management)
  * [Power Management](#power-management)
* [**Obstacle Management**](#obstacle-management)
  * [Sensor-Based Obstacle Detection](#Sensor-Based-Obstacle-Detection)
  * [Trajectory Calibration](#trajectory-calibration)
  * [Integration into the Robot's Program](#Integration-into-the-Robot's-Program)
* [**Photos**](#photos)
  * [Team Photos](#team-photos)
  * [Vehicle Photos](#vehicle-photos)
* [**Performance Videos**](#performance-videos)

***
## Our vehicle: 
![vehph](./v-photos/Car_components.PNG)
We used components from a EV3 MINDSTORMS Educational kit + a Pixy v2 Camera and some other technic pieces from other sets. 

A full list of all the components (not including the camera) can be found here: [Part List](models/part-list.pdf)

A 3D model of the robot made in Studio 2.0 can be found here: [3D Model](models/FE-Robot.io)
***

## Mobility Management

### Motor Selection and Implementation

Motor selection is a crucial component of our vehicle's autonomous navigation system. The Lego MINDSTORMS EV3 set provides two distinct motor options: Large Motors and Medium Motors. In making our selection, we considered key factors such as rotation speed, torque, and encoder accuracy.

![extract](./img/text.png)

The Large Motor offers substantial power, however, the Medium Motor, while less powerful, is smaller and lighter. This compact size facilitates quicker responses and conserves space within our vehicle design.
Given the constraints of our compact vehicle dimensions (300x200x300mm) and the emphasis on high-speed navigation, we prioritized the Medium Motor for both the steering and driving mechanisms. Our vehicle employs three Medium motors for its movement system: one for steering and two for driving.

### Chassis Design and Implementation

The steering mechanism, located in the front, utilizes smaller wheels, while the driving mechanism at the rear incorporates larger Lego Technic wheels placed closely together.
The placement of larger wheels at the rear serves multiple practical purposes. Larger wheels cover more ground per revolution, resulting in higher linear speed, which aligns with our priority for speed in the competition. Additionally, positioning the larger rear wheels as close to each other as possible, known as a "narrow rear track," mitigates the absence of a differential system. A narrow rear track minimizes the difference in wheel paths during turns, enhancing the vehicle's maneuverability and reducing wheel scrub.
![render](./img/robot.render.jpeg)
***

## Power and Sense Management

### Sensor Management

Our autonomous vehicle relies on a combination of sensors to execute precise movements, crucial for both obstacle avoidance and the qualification challenges of the competition.

Color Sensor: This sensor is employed to identify turns and determine the driving direction by reading colored lines (orange or blue) on the competition field.

Ultrasonic Sensor: Positioned at the front of the vehicle, the ultrasonic sensor measures the distance between the vehicle and field barriers, ensuring that the vehicle's relative position before and after a turn is continuously known.

Gyro Sensor: The gyro sensor plays a pivotal role in maintaining proper alignment. It detects changes in the vehicle's driving angle, alerting the system to any misalignment or deviation. The implementation of a PID (Proportional-Integral-Derivative) regulator ensures that any deviation from the desired steering angle is continuously corrected, guaranteeing the vehicle's straight and precise trajectory.

The PID regulator operates in a continuous loop throughout the program, ensuring the vehicle remains aligned and on the intended path, supporting its autonomous navigation capabilities.

Pixy v2 Camera: A camera is used to detect and differentiate obstacles during the obstacle round. Custom made 3D Print Models for the [cover](models/pixy_2_cover.stl) and the [case](models/pixy_2_case.stl) for the camera can be found in the corresponding links.

### Power Management
The power for the EV3 Brick and the whole vehicle comes from a rechargeable 10V Lithium Battery. Power management within the EV3 brick consists of multiple switching regulations which are tightly controlled and interlinked in order to boot the electronic circuit correctly.
To protect the EV3 brick from short circuit, 3 poly switches are included, one for each of the two motor drivers and one for the rest of the circuit. Each poly switch has a hold current at approximately 1.1 A and will be triggered at approximately 2.2 A.

Power Schemes for every electronic part of the vehicle can be found here:

[Color Sensor](schemes/color-sensor,pdf)

[Gyro Sensor](schemes/gyro-sensor.pdf)

[Medium Motor](schemes/medium-motor.pdf)

[Pixy v2](schemes/pixy2_schematic-2.2.pdf)

[Ultrasonic Sensor](schemes/ultrasonic-sensor.pdf)

[EV3 P-Brick](schemes/programmable-brick.pdf)

[Rechargeable Battery](schemes/rechargeable-battery.pdf)

[Ultrasonic Sensor](schemes/ultrasonic-sensor.pdf)

***

## Obstacle Management

Effective obstacle management is a critical aspect of our autonomous self-driving robot's navigation system, ensuring it can safely and intelligently navigate through challenging scenarios in the WRO competition. In this section, we elaborate on our obstacle management strategies and the key components involved in this crucial aspect of our robot's functionality.

### Sensor-Based Obstacle Detection

Our robot relies on a Pixy v2 Camera to detect obstacles, differentiating between red and green objects with precision. The camera's built-in plugin allows for the recognition of color-based signatures, making it a versatile and efficient tool for identifying obstacles.
To ensure accurate color detection, we employ PixyMon software to calibrate the camera. This calibration process fine-tunes the camera's color recognition capabilities, allowing our robot to precisely distinguish between red and green obstacles on the competition field.

![pixymon](./img/pixymon.jpeg)

### Trajectory Calibration
Calibrating the robot's trajectory is a vital step in ensuring it safely navigates around obstacles. This process involves placing obstacles in designated locations on the competition field and guiding the robot to drive around them. As the robot maneuvers around obstacles, we record the coordinates of these obstacles in a table for later analysis and fine-tuning.
Once the obstacle coordinates are collected, we import this data into software tools such as Microsoft Excel or Google Sheets. In these programs, we create graphical representations, which often take the form of exponential functions. This function encapsulates the ideal path for the robot to follow when circumventing obstacles.

![graph](./img/graph.jpeg)

### Integration into the Robot's Program
With the optimized obstacle-avoidance trajectory in hand, we proceed to integrate it into our robot's program. Our program includes a regulator designed to interpret and act upon the trajectory data.
This regulator operates in real-time, continuously assessing the robot's position in relation to the obstacles and adjusting its path accordingly. By using the trajectory data as a reference, the regulator guides the robot in a manner that ensures smooth and efficient obstacle avoidance. Additionally, a proportional-integral-derivative (PID) controller is employed to further fine-tune and enhance the robot's responsiveness when navigating around obstacles.

![program](./img/program.jpeg)

### Pseudo Code



***

## Photos

### Vehicle Photos
![vehph](./v-photos/Car_funny.PNG)
![vehph](./v-photos/1.jpg)
![vehph](./v-photos/2.jpg)
![vehph](./v-photos/3.jpg)
![vehph](./v-photos/4.jpg)
![vehph](./v-photos/5.jpg)
![vehph](./v-photos/6.jpg)

### Team Photos

![teamph2](./t-photos/t-official.jpeg)
![teamph](./t-photos/t-funny.jpeg)



***

## Performance Videos

Qualification Round Challenge: https://www.youtube.com/watch?v=faX3JqHLdDE

Obstacle Round Challenge: https://www.youtube.com/watch?v=62VS994mklY

Robot Parts Disscussion: https://www.youtube.com/watch?v=GfSPQbBEkag

***




