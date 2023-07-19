# Install a ready-to-use Ubuntu machine
## Install Ubuntu 18.04
Install a full desktop installation of Ubuntu 18.04 LTS. This is the version that ROS Melodic is compatible with.
For Hyper-v, you can use the quick-install feature for this.
## Connect the VM to the external network
Now you have to connect the VM to the external network. This is so that the VM can communicate with the robot and the robot can also talk back.
### Hyper-V
1. Open the Hyper-V Manager
1. Open the Virtual Switch Manager
1. Create a new "External" virtual switch
1. In the VM settings, connect the VM to the new virtual switch

### Static IP
If possible, setup a static IP adress in the Ubuntu network settings.
## Setup easy ssh connection for external use
### Setup ssh
1. Install openssh-server
    ```bash
    sudo apt install openssh-server
    ```
1. Enable ssh
    ```bash
    sudo systemctl enable ssh
    sudo systemctl start ssh
    ```
1. Setup ssh key
    On your host machine, generate a new ssh key if you don't have one already. (Windows: `ssh-keygen.exe`)
    ```bash
    mkdir ~/.ssh
    echo "[your public key]" > ~/.ssh/authorized_keys
    ```
1. Setup your ssh config file
    In `~/.ssh/config` add the following:
    ```
    Host rosvm-home
        HostName [vm ip address]
        User [vm username]
        IdentityFile ~/.ssh/[private key file]
    ```

## Base installation of ROS
Here we install the base ROS packages and set basic configurations.
It is important that we use ROS **Melodic** as this is the version the turtlebots have installed.  
We follow this tutorial: https://wiki.ros.org/melodic/Installation/Ubuntu
```bash
# select download mirror - choose the University of Freiburg for speed
sudo sh -c '. /etc/lsb-release && echo "deb http://packages.ros.org.ros.informatik.uni-freiburg.de/ros/ubuntu $DISTRIB_CODENAME main" > /etc/apt/sources.list.d/ros-latest.list'

# install curl
sudo apt install curl -y

# add the ROS key
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

# update the package list
sudo apt update

# install the full ros-melodic installation - this will take a while
sudo apt install ros-melodic-desktop-full -y

# install develpment tools
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential -y

# initialize rosdep
sudo rosdep init

# update rosdep
rosdep update
```

## Install the turtlebot3 packages
Now we install the turtlebot3 packages.

For now we only need the turtlebot3 slam package.
```bash
# install the turtlebot3 packages
sudo apt install ros-melodic-turtlebot3 ros-melodic-turtlebot3-slam -y
sudo apt-get install ros-melodic-dwa-local-planner -y
```

## Setup the Bashrc
Now we setup the bashrc file to automatically source the ROS environment and setup the ROS master URI.
```bash
# open the bashrc file
nano ~/.bashrc
```
Add the following lines to the end of the file:
```bash
source /opt/ros/melodic/setup.bash
export ROS_MASTER_URI=http://[vm ip address]:11311
export ROS_HOSTNAME=[vm ip address]
export TURTLEBOT3_MODEL=waffle
```

## X11 Window forwarding
If you want easy access without having to have the VM window open, you can setup X11 window forwarding.  
On the VM you either have to set the `DISPLAY` variable every time, or add it to the bashrc file.
```bash
# open the bashrc file
nano ~/.bashrc
```
Add the following line to the end of the file:
```bash
export DISPLAY=[ip of target/host machine]:0
```
On the target/host machine, you have to install an X11 server.
### Windows
On Windows, you can use [XMing](https://sourceforge.net/projects/xming/).  
Once you downloaded it, run `XLaunch` and use the following settings:
- One large window
- Start no client
- Disable access control