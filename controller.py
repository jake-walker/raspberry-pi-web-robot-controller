# load the flask module to create a web server
from flask import Flask, send_file

# load the gpiozero module to control the robot
from gpiozero import Robot

# make the web server
app = Flask(__name__)

# setup the robot
#  4 = the gpio pin on the pi for the left motor
#  8 = this gpio pin is not used
#  7 = the gpio pin on the pi for the right motor
#  10 = this gpio pin is not used
robot = Robot(left=(4,8), right=(7,10))

# setup a page route for sending the controller page
@app.route("/")
# now define a function which is called when this route is fetched
def controller():
	# this sends the main page that has the buttons to control the robot
	return send_file("controller.html")

# routes for controlling the robot

@app.route("/forward")
def forward():
	# when this page is requested make the robot go forward
	robot.forward()
	# send a message back so the browser knows the request was successful
	return "done"

@app.route("/left")
def left():
	robot.left(0.7) # i found leaving the speed at the default of 1
			# made the robot turn quickly and slowing the speed
			# made it easier to control
	return "done"

@app.route("/right")
def right():
	robot.right(0.7)
	return "done"

@app.route("/stop")
def stop():
	robot.stop()
	return "done"

# if this the entry point (run directly and not through another file) then..
if __name__ == "__main__":
	# start the web server on host 0.0.0.0 so it can be accessed
	# externally and not just on the pi, and port 80
	app.run(host="0.0.0.0", port="80")
