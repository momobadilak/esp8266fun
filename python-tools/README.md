# cheezecurl.py

This is a dirty little hack to test TCP and SSL functions of the ESP firmware.
I tried cutting & pasting the ESP AT commands into a serial window.. but that
quickly fell apart as soon as I tried to establish a TCP connection to a web server.


Between connecting to the web server and then pasting the 'GET' text, the webserver
would close the socket ...hence the reason for this script.


A secondary benefit is that working with python is even quicker and easier then
working in C via an arduino board. So, once I get things working in here reliably I'll move
back to C and the arduino micro.


## dependencies
pySerial - : http://pythonhosted.org/pyserial/index.html


  pip install pyserial


## works on my machine
 
I'm using Windows 10 on my laptop, but I also do ubuntu ... I think this should
work without too much hassle on that too.


Point the USEING_PORT variable at your /dev/ttyX device that works with minicom
and I think you should be up and running.
