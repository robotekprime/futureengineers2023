# Obstacle Detection and Color Recognition
Initialize PixyCamera
Set camera to color recognition mode

# Calibration
CalibrateCameraColorsUsingPixyMon()

# Trajectory Calibration
Initialize obstacleTable
Repeat for each obstacle in designated locations:
    Place obstacle on field
    Drive robot around obstacle
    Record obstacle's coordinates in obstacleTable

# Data Analysis and Path Creation
Import obstacleTable into Excel or Google Sheets

# Create Trajectory Function
CreateTrajectoryFunctionFromData()

# Robot Program
InitializeRobot()

Repeat Forever:
    ObstacleDetected, ObstacleCoordinates = PixyCamera.DetectObstacle()
    if ObstacleDetected:
        Path = CalculatePathToAvoidObstacle(ObstacleCoordinates, TrajectoryFunction)
        AdjustRobotPath(Path)
    else:
        ContinueFollowingPredefinedPath()
