# Virtual Mouse
An AI-based Mouse Controller using hand gestures in OpenCV.It is a virtual mouse control using fingertip identification and hand gesture recognition.
________________________________
## Technologies used:
Jupyter,OpenCV,autopy library, handTrackingModule

### HandTrackingModule
__________________________
Custom module created for tracking hands and returning hand related informations.
Used **[MediaPipe](https://google.github.io/mediapipe/getting_started/python.html)** for detecting hand gestures.
**HandDetector class** functions description: 

* **_findHands()_**

Detects hands and draw landmarks on the hand and between two successive landmarks a line is drawn.

* **_findPosition()_**

It returns the list of the positions of all the landmarks of the hands which are detected.

* **_fingersUp()_**

return a list of size 5 which have binary values, 0 denotes particular index finger is down and 1 denotes that particular indexed finger is up.

* **_findDistance()_**

Returns coordinates of the first landmark (provided the index ), coordinates of the second landmark(provided the index) and the coordinates of their centre. Also, it draws a line between these two landmarks.
_______________________________

### Autopy 
AutoPy is a simple, cross-platform GUI automation library for Python. It includes functions for controlling the keyboard and mouse, finding colours and bitmaps on-screen, and displaying alerts.
[AutoPy GitHub link](https://github.com/autopilot-rs/autopy)
_________________________________
### Simulation of Virtual Mouse
https://user-images.githubusercontent.com/61883605/134120725-c7aeb748-7044-4ee2-b282-51ef14f8499a.mp4
### Working 
In this particular simulation, when the index finger and middle finger are stick together, it acts as a moving mouse pointer while if we put down the middle finger, the pointer will click on that particular instance.
__________________________________
