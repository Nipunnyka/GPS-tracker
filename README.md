# GPS-Tracker
 This application plots the live path of a rover fitted GPS tracker through Arduino on a GMaps API. Developed so that we can ensure the rover is following the corrent trajectory in autonomous navigation task at IRC.
The following are the characterstics of this project:
* Server-Client Architecture
 * Arduino scripts (in C++) to send properly formatted location coordinates of the rover
 * WebSocket to connect to Arduino (written in Python) and fetch current latitude and longitude of rover which also continuosly listens for connections
 * Client side webapp which connects to a ip and initiates websocket asking for live location and plots it in real time 
Note: API key is outdated now
The following caveats have to be followed:
* Rover should have a static IP address
* Special points are set of way points through which the rover has to traverse

How to run the application
1. Upload the Arduino scripts inside `Arduino_GPS_code` to the Arduino Board
2. Run `websocket-trial.py` on the on-board computer 
```
python3 websocket-trial.py
```
3. Open `index.html` on your client computer and enter the required information



The following is an image of the application, the rover is in storage and there is no way t obtain a working screenshot now, meanwhile please make do with a connectionless front-end:
![image of the web-app](/images/ss.png)
