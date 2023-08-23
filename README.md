Engineering materials
====

This is the official repository of the Robotek Prime team. It contains all the engineering materials of our self-driven vehicle's model participating in the WRO Future Engineers competition in the season 2023.

<h2 tabindex="-1" dir="auto"><a id="user-content-content" class="anchor" aria-hidden="true" ><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"></svg></a>Mobility Management:</h2>
<a id="user-content-introduction" class="anchor" aria-hidden="true" href="#introduction">Mobility Management:</a>

The mobility management of our Lego Mindstorms EV3 robot forms the core of its autonomous navigation capabilities. Designed to excel in the dynamic challenges of the WRO competition, our robot's movement strategy combines a range of carefully selected components and sensors to achieve precise control and efficient motion.

Motor Selection and Implementation:
Our robot is equipped with two drive motors connected to a single driving axle, eliminating the need for a differential mechanism. These motors were chosen for their compatibility with the Lego Mindstorms EV3 platform, ensuring seamless integration and reliable performance. To enhance straight-line movement accuracy, a gyroscope sensor is employed to provide real-time feedback on the robot's orientation. This feedback is utilized to make subtle adjustments to the motor outputs, ensuring the robot maintains a consistent heading even during slight deviations.

Steering Actuator:
For effective steering, our robot features a dedicated steering actuator that enables controlled turns. Adhering to the competition's rules, our vehicle employs a single steering actuator, providing simplicity and precision in turning maneuvers. By combining data from the gyroscope and the ultrasonic distance sensor, our robot accurately gauges its proximity to the track's inner walls, allowing it to execute turns with minimal deviation and maximizing its chances of staying on the optimal racing line.

Line Following Strategy:
To handle turns accurately, our robot employs a color sensor positioned strategically on the front of the chassis. This sensor detects lines placed before the turns on the track, allowing the robot to anticipate upcoming curves. Upon detecting a line, the robot triggers a predefined turning algorithm that adapts based on the type of line (green or red) and the information from the gyroscope. This combination of sensors and algorithms ensures precise timing and execution of turns, minimizing speed loss and maintaining efficiency.

Obstacle Detection and Avoidance:
The Pixy camera mounted atop our robot is a critical component for obstacle detection. It identifies the distinct green and red pillars placed on the track, allowing the robot to react promptly. Upon detection of a pillar, the robot adjusts its path accordingly to avoid collisions. The integration of the Pixy camera enables the robot to not only detect obstacles but also assess their position and take appropriate evasive actions.

In conclusion, our robot's mobility management system exemplifies a holistic approach to navigation, integrating sensors like the gyroscope, ultrasonic sensor, color sensor, and Pixy camera. The combination of these components allows our robot to maneuver accurately, follow the racing line, and detect and avoid obstacles, showcasing a robust and well-coordinated mobility strategy for the WRO competition's dynamic challenges.
