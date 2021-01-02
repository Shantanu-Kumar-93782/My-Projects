# Task-Distributor
This project is a prototype for dividing a simple task and distributing among available systems in same Network.
Currently this project implements password cracking where you have hash available of a password and you want to crack it.


Now to use this project following dependencies should be fulfilled:-
  1. Crunch tool should be available on slave machines.
  2. Gtk 3.0 library should be available on master as well as slave machines. 
 
How it works:-
  Sample folder represents a slave machine, so if you want to make a machine act as slave just copy the content of folder on to the machine. Run slave.py and machine.py
  respective machine. Currently total number of slaves allowed are 20. Now once you start Master.py, you have to enter ip to which slaves will contact. Now just give 
  hash you want to crack, what kind of hash it is, size of password (just guess this and try for different lengths). 
  
  Choose type of wordlists (Note if you define predefined then that list should be present in slave's machine with name as "predefined.txt". Once done, just connect the 
  slaves to the master, you can check wehter they are connected or not in statistics tab. And then click start, after this tasks are allocated to slaves, now slaves have
  to click start to accept the task and start working on them.
  
  You can see the progress of each slave in statistics tab. If the hash is successfully cracked it will be shown in the log area of master.
