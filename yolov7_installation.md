# How to install yolov7 on jetson nano
We are following this very simple tutorial: [YOLOv7 on Jetson Nano](https://i7y.org/en/yolov7-on-jetson-nano/)
## Clone the git repo
```bash
cd ~
git clone https://github.com/WongKinYiu/yolov7
```
## Setup the environment 
### Install python headers
```bash
sudo apt-get install gcc python3.8-dev
```
### Install specific python version (3.8)
```bash
sudo apt-get install python3.8
```
### Setup venv
```bash
cd ~/yolov7
mkdir venv
python3.8 -m venv ./venv/
source ./venv/bin/activate
```
### Update pip
```bash
python3.8 -m pip install --upgrade pip
```
### Install requirements
```bash
python3.8 -m pip install -r requirements.txt
```
### (Optional) Install rospy and rospkg
Only if you want to change the detect.py script locally.
```bash
python3.8 -m pip install rospy rospkg
```


## Run the demo
```bash
python3.8 detect.py --source 0```