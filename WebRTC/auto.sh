#!/bin/bash

dbus-launch gnome-terminal --"/home/jacky/Desktop/WebRTC/WebRTC" -e "ngrok start --all"
dbus-launch gnome-terminal --"/home/jacky/Desktop/WebRTC/WebRTC" -e "python3 /home/jacky/Desktop/WebRTC/WebRTC/Line.py"