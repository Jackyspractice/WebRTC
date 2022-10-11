#!/bin/bash

gnome-terminal --"/home/jacky/Desktop/WebRTC/WebRTC" -e "ngrok http 5000"
gnome-terminal --"/home/jacky/Desktop/WebRTC/WebRTC" -e "python3 Line.py"