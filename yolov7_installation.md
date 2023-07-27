# How to install yolov7 on jetson nano
We are following this tutorial: [Yolov7 deoply on jetson nano](https://www.hackster.io/spehj/deploy-yolov7-to-jetson-nano-for-object-detection-6728c3)  

## Virtual environment
Instead of using the virtual environmnet method they propose, we used the more barebones version instead like this:
```bash
cd ~
git clone https://github.com/WongKinYiu/yolov7
cd ~/yolov7
python3.6 -m venv ./venv3.6/
source venv3.6/bin/activate
```

Now follow all the steps of the tutorial after the `deactivate` codeblock.