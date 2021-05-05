# cs370-group-project

This project connects the XBox360 Kinect Sensor to the Rasperry Pi, allowing the user to access the color and depth data from the Kinect from any location by using a webserver. 

The libfreenect library and drivers for ARM systems is a prerequisite for this program and can be found at the following location. 
https://github.com/OpenKinect/libfreenect

With libfreenect installed, first the user must run the async.py program. This will activate the Kinect Sensor and tell it to start recording data and updating the current view images. 

The async.py program needs to be run with python3 and needs sudo privilages to access the data stream. 

Next, the server.py program is run in a new console. This program starts a flask web server on the local host and displays a webpage with the data from the kinect. The webserver is configured so that browser caching is disabled to allow the user to always refresh for a live view from the kinect. 

If any both images are not shown, a refresh should fix the page. 
