# Get ready your computer ready for the course

If you are joining us for this course or plan to try this material on your own, here is our plan to get you started and running the exercises.

### 0. If you have windows you need to start here (except you can start from 1).

You need to have WSL the ***Windows subsystem for Linux*** (only Windows users). 

**a.** You will need windows 10 (version 2004 and higher) or windows 11!

**b.** Open the CMD terminal and install WSL `wsl --install`, now you can install your linux distribution

**c.** To have a list of the linux distributions available `wsl --list --online`. Get the most up-to-date but not beta version.

**d.** To install or update your version use `wsl --install -d <dist_name>`, in this case we suggest **Ubuntu-20-04** 

> You can use WSL terminal on Windows or use the VSCode terminal with WSL. To  ***enable WSL*** in VSCode follow bellow:
>
> - press F1 and search/choose **WSL: Connect to WSL**
>
> - press F1 and search/choose **Terminal: Select Default Profile**
>
>  - choose the **Ubuntu-Version (WSL)** option

### 1 . You will need to have **Docker desktop** installed so you run it locally.

  for [Windows](https://docs.docker.com/desktop/install/windows-install/)

  for [MAC](https://docs.docker.com/desktop/install/mac-install/)
  
  for [Linux](https://docs.docker.com/desktop/install/linux-install/)

> You will need to enable WSL if you are using windows. 

### 2. Get any text editor to work
Suggestion: [VScode](https://code.visualstudio.com/download) , [Sublime text](https://www.sublimetext.com/3),  [Emacs](https://www.gnu.org/software/emacs/download.html)

**a.** If you decide to use VSCode terminal instead of your native terminal, you will need to install extensions to have docker running. 

- Docker : that is the extension needed to run docker.

**b.** Install git in WSL or on your MAc/Linux terminal by running the line `sudo apt-get install git` don't forget to setup the config file

```
git config --global user.name "Your Name"
git config --global user.email "youremail@domain.com"
```

### 3. You will need to clone the repository with the data and activities

**a.** If you are using MAC or Linux, you should be able to do to

```
git clone https://github.com/vibbits/containers-workshop.git
```

### 4. Set your VSC account

* 3.1	  **Register** for an [HPC account](https://docs.vscentrum.be/access/vsc_account.html) before the course since it might take some time to process and activate. 

> P.s.: If you are from industry or in any other situation where you are not linked to an academic institution we can only help you get an account when registered in the VIB course, check avaiability in [VIB training website](https://training.vib.be/?tags%5B103%5D=103).

3.2 Once you have an account, you can [access it](https://account.vscentrum.be/), and you will be able to see your VSC ID, and other information about your account. Eventually you might want to add an SSH key to connect remotely. You will not need this for this session.

3.3 Test if it you can connect:

Visit [login page](https://login.hpc.ugent.be) , the 1st time you do it permission will be requested to let the web portal access some of your personal information, authorize it!!  Once logged in, you should see this start page!
