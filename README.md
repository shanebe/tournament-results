# tournament-results
P2: Tournament Results

# Environment Instructions
- Install VirtualBox
VirtualBox is the software that actually runs the VM. You can download it from virtualbox.org, <a href="https://www.virtualbox.org/wiki/Downloads">here</a>. Install the platform package for your operating system.

- Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.  You can download it from vagrantup.com, <a href="https://www.vagrantup.com/downloads">here</a>. Install the version for your operating system.

- Clone the Vagrant VM COnfiguration from GitHub

> git clone http://github.com/udacity/fullstack-nanodegree-vm fullstack

- Boot up and log into the Virtual Machine
Using the terminal, change directory to fullstack/vagrant 

> cd fullstack/vagrant

then type 

> vagrant up 

to launch your virtual machine.

To log in to your machine 

> vagrant ssh

# Project Instructions

- Once logged into your vagrant environment, clone the project 

> git clone https://github.com/shanebe/tournament-results.git

- Move into this folder and use PSQL to import the database SQL file

> psql

> \i tournament.sql

- You are now ready to run the Tournament Test python file!

> python tournament_test

- Expected results are as follows:

Old matches can be deleted.
Player records can be deleted.
After deleting, countPlayers() returns zero.
After registering a player, countPlayers() returns 1.
Players can be registered and deleted.
Newly registered players appear in the standings with no matches.
After a match, players have updated standings.
After one match, players with one win are paired.
