# How to install YOLO on jetson nano
## clone git repo
```bash
git clone https://github.com/WongKinYiu/yolov7
```
## install requirements
```bash
sudo apt install python3.8 python3-venv gcc python3.8-dev python3.8-setuptools -y
```
## create venv
```bash
cd yolov7
mkdir venv
python3.8 -m venv ./venv
source ./venv/bin/activate
```
## update pip
```bash
pip install --upgrade pip
```
## install requirements
```bash
pip install -r requirements.txt
```
## launch it to confirm if it works
```bash
python3.8 detect.py --source 0
```
