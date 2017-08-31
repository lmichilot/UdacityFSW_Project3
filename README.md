# Project 3: Logs Analysis Project
### by Luis Michilot

## What it is and does

A Python program that prints out reports (in plain text) based on the data 
in the database. This reporting tool is using the psycopg2 module to 
connect to the database.

## Required Libraries and Dependencies

* Python 3.x is required to run this project.
* PostgreSQL 9.5 or latest version.

## Project contents

This project consists for the following files:

* reporting.py - (program source code)
* result_report.txt - (program result)
* newsdata.zip - (contains the table and views definition for the project)

## How to Run Project

* Install Vagrant and VirtualBox
* Clone this repository
* Unzip file `"newsdata.zip"`. The file inside is called newsdata.sql. 
  Put this file into the vagrant directory, which is shared with your virtual 
  machine.
* Launch Vagrant VM by running `vagrant up`, you can the log in with `vagrant ssh`  
* To load the data, use the command `psql -d news -f newsdata.sql`
* Navigate to the project directory and type `python reporting.py` from the command
  line. 



