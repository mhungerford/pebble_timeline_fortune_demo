# pebble_timeline_fortune_demo
Pebble timeline app showing random daily fortunes.  Extremely minimal app (python, js, c) to help beginners.

Based off of the Daily Fortune app for Timeline in the Pebble appstore (removed universal timezone support to simplify example)  
https://apps.getpebble.com/applications/55af2f53ac7b440eed000038
![Daily Fortune](https://www.filepicker.io/api/file/JCMdtCzkTD1XyA36bDAp/convert?h=160&w=360)

![Fortune](https://www.filepicker.io/api/file/DHCuKERS3yXkCXuf24YM/convert?h=168&w=144)

## Uses 
* pypebbleapi for timeline pins with subscription 
** [fortune_timeline.py](pythonanywhere.com/fortune_timeline.py) = 21 lines of code
* pebble javascript subscribing user to fortune timeline topic 
** [pebble-js-app.js](src/js/pebble-js-app.js) = 9 lines of code
* minimal required c application running on watch 
** [fortune_timeline.c](src/fortune_timeline.c) = 5 lines of code

## PythonAnywhere.com
Original Daily Fortune Timeline Server was hosted using the free pythonanywhere.com
As it has almost no setup overhead 
* create free account
* upload python file (or edit using their browser-based text editor)
* enter time to schedule python code to run on the server (or click run button to test)

## Fortunes
Additionally this example includes a python3 supported version of fortune.py, based off the command-line fortune app, providing fortunes and quotes from fortune files.
[fortune.py](pythonanywhere.com/fortune.py)

