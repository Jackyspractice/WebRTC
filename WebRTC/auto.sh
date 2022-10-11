#!/bin/bash

dbus-launch gnome-terminal --"/home/jacky/Desktop/WebRTC/WebRTC" -e "ngrok http 5000"
dbus-launch gnome-terminal --"/home/jacky/Desktop/WebRTC/WebRTC" -e "python3 /home/jacky/Desktop/WebRTC/WebRTC/Line.py"