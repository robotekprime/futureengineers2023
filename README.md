
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
  *[Sensor Management](#sensor-management)
  *[Power Management](#power-management)
* [**Obstacle Management**](#obstacle-management)
* [**Photos**](#photos)
  * [Team Photos](#team-photos)
  * [Vehicle Photos](#vehicle-photos)
* [**Performance Videos**](#performance-videos)
* [**Conclusion**](#conclusion)

***
## Our vehicle: 
![render](./img/robot.render.jpeg)

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

![battery](./img/battery.jpg)
***

## Obstacle Management

***

## Photos

### Team Photos

### Vehicle Photos

***

## Performance Videos

***

## Conclusion

***




