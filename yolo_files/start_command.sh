#!/bin/bash
# This script is used to start the yolo detection
cd ~/yolov7
source venv3.6/bin/activate
python3 detect.py --weights yolov7-tiny.pt --conf 0.25 --img-size 1280 --no-trace --source Blank_16_9.jpg
