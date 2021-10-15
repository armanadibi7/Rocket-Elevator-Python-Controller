# Rocket-Elevators-PYTHON-Controller
This is a source code to Rocket Elevators Controller written in PYTHON by Arman Adibi.

The test files make sure that the Controller are working correctly and it is safe
to be implented into our customers building.

Installation

First, depending on your python version, make sure to install the Package Installer for Python (PIP) if needed:

https://pip.pypa.io/en/stable/installing/

Next, install Pytest:

https://docs.pytest.org/en/6.2.x/getting-started.html

WHEN ALL THE REQURIMENTS ARE THERE:

    TO RUN THE TEST , TYPE IN YOUR CONSOLE:
        pytest
    You can also get more details about each test by adding the -v flag:

    pytest -v

============== CONTENTS OF THIS PYTHON SOURCE CODE ============== 
1. Column

        * DECLARE ITS ATTRIBUTES (CONSTRUCTORS)
        * CREATE ELEVATORS OBJECTS INSIDE EACH COLUMNS
        * CREATES BUTTONS OUTSIDE THE ELEVATORS(WHICH HANDLE THE FIRST REQUEST FOR AN ELEVATOR)
        * FIND THE NEAREST ELEVATOR( MATH FUNCTION : FLOOR RQUESTED FROM - ACTUAL POSITION => WHICH ON IS CLOSEST TO 0)
        * SEND THE ELEVATOR TO IT DESTINATION
        
2. ELEVATOR

        * HANDLE ELEVATOR ATTRIBUTES
        * CREATE BUTTONS INSIDE THE ELEVATORS
        * WAIT FOR AN DESTINATION FLOOR
        * MOVE THE ELEVATOR THROUGH THE QUEUE LIST UNTIL THERE IS NO MORE REQUEST
        * OPERATES THE DOOR OF THE ELEVATOR

3. CALLBUTTON

        * HANDLE THE OUTSIDE BUTTONS ATTRIBUTES

4. FLOORRQUESTBUTTON:

        * HANDLE THE INSIDE BUTTONS ATTRIBUTES

5. DOORS:

        * HANDLE THE DOORS ATTRIBUTES


============== THE LOGIC OF THIS PYTHON SOURCE CODE ============== 


We receive a request for an elevator, the elevator move to the request floor.
Open its door and wait for the Client to enter his destination floor.
We add this destination floor to the queue list(List of the floors to be done).

How Do we select an elevator: 


    * We check it's status first
    * If idle, we add it to the list of possible elevator
    * If moving, but it's moving to the same direction as the requested floor
    * We check the gap betweeen the request floor and the current floor of the elevator
    * Which elevator's gap is closest to the 0, it's the one that is chosen.
    
