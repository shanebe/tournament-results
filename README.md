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
- tournament.sql is where you will put the database schema, in the form of SQL create table commands
- tournament.py is where you will put the code for your tournament module.
- tournament_test.py contains test functions that will test the functions you’ve written in intournament.py

To run the series of tests defined in this test suite, run the program from the command line 
> python tournament_test


