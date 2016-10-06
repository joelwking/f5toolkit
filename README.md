# f5toolkit
F5 Tool Kit for Network Engineer Ephemeral Tooling.

## Overview
One challenge in teaching network engineers infrastructure automation techniques is easily enabling an environment for them to consume the automation tools and techniques. Vagrant is a software package which automates the creating and configuration of virtual machines in Oracle VirtualBox. By installing VirtualBox and Vagrant, the network engineer can  consume these lab exercises without the system administation burden of setting up all the necessary components.

This repository represents the concept of an ephemeral tool- allowing network engineers to experiment with [F5 Python SDK] (https://f5-sdk.readthedocs.io/en/latest/index.html) and [Ansible] (https://ansible.com) playbooks to automate the configuration of F5 BigIP using the iControl REST interface.

## Prerequisites
The installation and execution steps assume that [GitShell] (https://desktop.github.com/), [Vagrant] (https://www.vagrantup.com/) and [Oracle VM VirtualBox] (https://www.virtualbox.org/) are installed. The documentation steps are shown on a Windows 7 laptop.

## Installation
Create a directory, enter it, and download the Vagrantfile. If curl is not installed you can edit the file on your local machine and cut and paste the commands into the Vagrantfile.
```
C:\Users\kingjoe\Documents\WWT\projects\Vagrant>

mkdir f5toolkit
cd f5toolkit
curl -o Vagrantfile https://raw.githubusercontent.com/joelwking/f5toolkit/master/Vagrantfile

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  3733  100  3733    0     0   8342      0 --:--:-- --:--:-- --:--:-- 12199

```
## Execution
Bring up the virtual machine.
```
vagrant up
```
SSH into the virtual machine.
```
vagrant ssh

vagrant@vagrant-ubuntu-trusty-64:~$ ls
f5toolkit
vagrant@vagrant-ubuntu-trusty-64:~$ cd f5toolkit/
vagrant@vagrant-ubuntu-trusty-64:~/f5toolkit$ ls
ansible  bin  LICENSE  README.md  Vagrantfile
```
### Python SDK lab
The sample Python program illustrates the use of the F5 Python SDK. [https://f5-sdk.readthedocs.io/en/latest/index.html]

Edit the constants file and replace the F5 BigIP hostname, username and password. The Python program will import this file and use the values to connect and authenticate with the F5 BigIP.
```
root@vagrant-ubuntu-trusty-64:/home/vagrant/f5toolkit# sudo vi ./bin/constants.py
```
Now log on the GUI of the F5 BigIP and run the program. The program prompts you to continue at each step to allow an opportunity to view the changes made to the LTM Pools using the GUI.
```
vagrant@vagrant-ubuntu-trusty-64:~/f5toolkit$ python ./bin/python-sdk-for-big-ip.py
NEW_POOL1
                NEW_NODE1:80
                NEW_NODE2:80
NEW_POOL100
                NEW_NODE101:80
NEW_POOL200
                NEW_NODE201:80
mediaWIKI
                xStart1456757786:80
test_monitor_pool
                NODE_NAME:80
Created new pool: mypool, press return to continue.
Added description to pool: mypool, press return to continue.
Attempted to delete pool 'foo', press return to continue.
Attempted to delete pool: mypool, press return to continue.
vagrant@vagrant-ubuntu-trusty-64:~/f5toolkit$
```
### Ansible F5 playbook lab
From the F5 BigIP GUI, verify the LTM node `foo` does not exist. Delete as necessary.

Enter the Ansible playbook directory
```
vagrant@vagrant-ubuntu-trusty-64:~/f5toolkit$ cd ansible/playbooks/
```
Run the playbook to create an LTM node
```
vagrant@vagrant-ubuntu-trusty-64:~/f5toolkit/ansible/playbooks$ sudo ansible-playbook create_ltm_node.yml
Enter F5 IP address: vf5-mediawiki.sandbox.wwtatc.local
Enter username: admin
Enter password:

PLAY [localhost] ***************************************************************

TASK [Create LTM Node] *********************************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=1    changed=1    unreachable=0    failed=0
```
Verify on the F5 BigIP GUI that the LTM node `foo` has been created.

### Automate F5 Initial Setup - iControl & Ansible
This lab illustrates how to automate the entire F5 initial setup by reading a CSV file and running an Ansible playbook.

*ADD ME*

### Destroy the Lab
Logoff the virtual machine and destroy it.
```
vagrant@vagrant-ubuntu-trusty-64:~/f5toolkit/ansible/playbooks$ exit
logout
Connection to 127.0.0.1 closed.

C:\Users\kingjoe\Documents\WWT\projects\Vagrant\f5toolkit>vagrant destroy
    default: Are you sure you want to destroy the 'default' VM? [y/N] y
==> default: Forcing shutdown of VM...
==> default: Destroying VM and associated drives...
```
