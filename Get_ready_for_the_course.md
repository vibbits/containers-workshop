# Get ready your computer ready for the course

If you are joining us for this course or plan to try this material on your own, here is our plan to get you started and running the exercises.

### 0. If you have windows you need to start here (except you can start from 1).

You need to hae WSL the ***Windows subsystem for Linux*** (only Windows users). 

**a.** You will need windows 10 (version 2004 and higher) or windows 11!

**b.** Open the CMD terminal and install WSL `wsl --install`, now you can install your linux distribution

**c.** To have a list of the linux distributions available `wsl --list --online`. Get the most up-to-date but not beta version.

**d.** To install or update your version use `wsl --install -d <dist_name>`, in this case we suggest **Ubuntu-20-04** 

### 1 . You will need to have **Docker desktop** installed so you run it locally.

  for [Windows](https://docs.docker.com/desktop/install/windows-install/)

  for [MAC](https://docs.docker.com/desktop/install/mac-install/)
  
  for [Linux](https://docs.docker.com/desktop/install/linux-install/)

> You will need to enable WSL if you are using windows.

### 2. Get VScode (*Virtual Studio Code*) on your computer. It will be your terminal and your editor during this journey.

**a.** Install [VScode](https://code.visualstudio.com/download) in your system. If you are using MAC or Linux, you can use your own local terminal and your favorite editor. But you can also install VScode using the link above.

**b.** You will need to install extensions to have docker running in VScode and to be able to make SSH connection for the part of the course that will happen in the VSC (***Vlaams Supercomputer***).

- Remote-ssh : that is the extension to connect via ssh key.   
- Docker : that is the extension needed to run docker.

**c.** If you are using windows you need to ***enable WSL***  and to choose the WSL terminal. 

- press F1 and search/choose **WSL: Connect to WSL**

- press F1 and search/choose **Terminal: Select Default Profile**

- once you have choose the **Ubuntu-Version (WSL)** option

- install git in WSL by running the line `sudo apt-get install git`

- don't forget to setup the config file

```
git config --global user.name "Your Name"
git config --global user.email "youremail@domain.com"
```

### 3. You will need to clone the repository with the data and activities

**a.** If you are using MAC or Linux, you should be able to do to

```
git clone <ssh_address>
```

**b.** if you are using Windows, you will open VScode and find the Welcome page or press `ctrl+shift+G` and choose **Clone repository** > **Clone from github** > **ssh_address**

choose the folder to keep your repository and develop the course.
