# Raspberry Pi Web Robot Controller
A simple web-based Raspberry Pi Robot Controller

![](robot.jpg | width=250px)

I was lucky enough to win a trip to the Raspberry Pi Pioneers Summer Camp at Google HQ, and while I was there I needed to write a simple Python program to let me control the robot I built in just an hour (including testing time!) so I recreated what I made and put it on GitHub for people to check out (because I had to rewrite it all because I left my SD card there).

## What You'll Need

- [ ] A working robot/buggy *([Build Instructions](https://projects.raspberrypi.org/en/projects/build-a-buggy))*
- [ ] Your Pi's IP address (`ifconfig`)
- [ ] An internet connection for your Pi

## Setup

### Installing required modules

*If you have the SD card from the Pioneers Summer Camp (I found) that `gpiozero` and `flask` were already installed.*

The only things you need should be `gpiozero` and `flask`, and everything else should be already included with the full Raspbian and the console-only version.

```
sudo apt update
sudo apt install python-gpiozero python-flask
```

### Installing the Controller

```
git clone https://github.com/jake-walker/raspberry-pi-web-robot-controller.git
```

## Running

```
cd raspberry-pi-web-robot-controller
sudo python controller.py
```

**The second command must be run as sudo as it uses port 80.**

Then go to your Pi's IP on your phone (or any other device) as long as it's on the same network and control it.
