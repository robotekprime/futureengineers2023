Engineering materials
====

This is the official repository of the Robotek Prime team. It contains all the engineering materials of our self-driven vehicle's model participating in the WRO Future Engineers competition in the season 2023.

<h2 tabindex="-1" dir="auto"><a id="user-content-content" class="anchor" aria-hidden="true" ><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"></svg></a>Mobility Management:</h2>

The mobility management of our Lego Mindstorms EV3 robot forms the core of its autonomous navigation capabilities. Designed to excel in the dynamic challenges of the WRO competition, our robot's movement strategy combines a range of carefully selected components and sensors to achieve precise control and efficient motion.

Motor Selection and Implementation:
Our robot is equipped with two drive motors connected to a single driving axle, eliminating the need for a differential mechanism. These motors were chosen for their compatibility with the Lego Mindstorms EV3 platform, ensuring seamless integration and reliable performance. To enhance straight-line movement accuracy, a gyroscope sensor is employed to provide real-time feedback on the robot's orientation. This feedback is utilized to make subtle adjustments to the motor outputs, ensuring the robot maintains a consistent heading even during slight deviations.

Steering Actuator:
For effective steering, our robot features a dedicated steering actuator that enables controlled turns. Adhering to the competition's rules, our vehicle employs a single steering actuator, providing simplicity and precision in turning maneuvers. By combining data from the gyroscope and the ultrasonic distance sensor, our robot accurately gauges its proximity to the track's inner walls, allowing it to execute turns with minimal deviation and maximizing its chances of staying on the optimal racing line.

Color Detecting Strategy:
To handle turns accurately, our robot employs a color sensor positioned strategically on the front of the chassis. This sensor detects lines placed before the turns on the track, allowing the robot to anticipate upcoming curves. Upon detecting a line, the robot triggers a predefined turning algorithm that adapts based on the type of line (orange or blue) and the information from the gyroscope. This combination of sensors and algorithms ensures precise timing and execution of turns, minimizing speed loss and maintaining efficiency.

Obstacle Detection and Avoidance:
The Pixy camera mounted atop our robot is a critical component for obstacle detection. It identifies the distinct green and red pillars placed on the track, allowing the robot to react promptly. Upon detection of a pillar, the robot adjusts its path accordingly to avoid collisions. The integration of the Pixy camera enables the robot to not only detect obstacles but also assess their position and take appropriate evasive actions.

In conclusion, our robot's mobility management system exemplifies a holistic approach to navigation, integrating sensors like the gyroscope, ultrasonic sensor, color sensor, and Pixy camera. The combination of these components allows our robot to maneuver accurately, follow the racing line, and detect and avoid obstacles, showcasing a robust and well-coordinated mobility strategy for the WRO competition's dynamic challenges.








<h2 tabindex="-1" dir="auto">Power and Sense Management:</h2>

The seamless integration of power and sense management lies at the heart of our Lego Mindstorms EV3 robot's ability to navigate the diverse challenges presented by the WRO competition. This section illuminates the selection of power sources, the rationale behind sensor choices, and the meticulous orchestration of power consumption for optimal performance.

**Power Source and Management:**
Our robot draws its energy from a high-capacity rechargeable lithium-ion battery pack, meticulously chosen to provide sustained power throughout the competition rounds. This battery pack supplies consistent voltage and current to all essential components, ensuring uninterrupted operation and allowing the robot to maintain peak performance over the duration of the challenges. Advanced power management algorithms are implemented within the EV3 brick to regulate voltage levels and prevent power fluctuations that could impact the robot's accuracy and responsiveness.

**Sensor Selection and Integration:**
The selection of sensors is a key determinant in our robot's adaptability to the varied challenges of the competition. The ultrasonic sensor, for instance, plays a pivotal role in assessing the distance to the inner walls of the circular track. By emitting ultrasonic pulses and measuring the time taken for their return, this sensor enables the robot to precisely gauge its proximity to the walls, facilitating optimal steering control during turns.

Our robot's color sensor, strategically positioned at the front, interprets the color of the track lines and the traffic signs. This sensor assists the robot in executing well-timed turns and interpreting the instructions conveyed by the color-coded signs, contributing to the vehicle's strategic decision-making.

The Pixy camera's integration, a testament to our robot's versatility, extends its perceptual capabilities. This camera captures visual data of the track environment, allowing our robot to distinguish between green and red pillars. By recognizing these obstacles, the robot can calculate their positions relative to its trajectory and make split-second decisions to avoid collisions.

**Power Consumption Optimization:**
To ensure sustained operation, our robot employs an energy-conscious approach to power consumption. For example, sensors are activated only when necessary, conserving energy without compromising functionality. The gyroscopic sensor, for instance, is utilized selectively to maintain a straight trajectory, activated periodically to make subtle course corrections. Similarly, the Pixy camera's processing load is managed dynamically, with advanced algorithms identifying moments where obstacle detection is essential.

In conclusion, our robot's power and sense management strategy harmonizes energy efficiency with sensor efficacy. Through meticulous sensor selection, strategic integration, and power-conscious design, our robot strikes a balance between performance and sustainability. This combination empowers our robot to intelligently navigate the challenges with precision, responsiveness, and an adaptive use of resources.

