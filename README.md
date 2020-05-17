# Path Planning and Obstacle Avoidance
## Team Rakshak, IIT Bombay

To run the simulation, run **circletracer.py**.

This program requires **pygame** package as a requirement.

Install Pygame by executing `pip install pygame` in the terminal.

### Algorithm Explanation
1. First accept all the waypoints and initiate all the obstacles.
    - Waypoint is of form `({X_coordinate}, {Y_coordinate})`
    - Obstacle is of form `({X_coordinate_of_Centre}, {Y_coordinate_of_Centre}, {Radius})`
2. Increase the radius of all obstacles by a `grace` amount
3. Rearrange the waypoints from start to end by lowest distance greedy approach.
4. For each successive pair of waypoints, generate path between them.
    - If there is no obstacle between two points
        - Directly join them by a line
    - Else, 
        - for each obstacle in obstacles
            - Join `start_point` to intersection of direct line and obstacle by a straight line.
            - Trace the obstacle's circumference until next intersection point of line and obstacle in such a way that shortest arc is traced.
            - Set `start_point` to the second intersection and repeat for next obstacle.
        - Join the last point to the `end_point`
        
