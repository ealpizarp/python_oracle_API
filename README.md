# python_oracle_API

A simple python Rest API that connects with an oracle database. It supports
the following requests: `PUT`, `POST`, `DELETE` and `GET`, the testing of these
can be done with postman or insomnia. 

## Create virtual enviroment

For creating the virtual enviroment in order to install the dependencies:

`python -m venv .venv`

Activate the virtual enviroment

`.venv\scripts\activate.bat`

Install the dependencies

`pip install -r requirements.txt`

Run the rest api

`python python_api.py`

You're all set!



## React web interface

To run the react web interface it's required to have installed Node.js and bootstrap 
installed via npm. Once you have downloaded this programs you wull need not create a 
react app.

The react app can be instaciated with the following commands:

`npx create-react-app my-app`

Change directory to the new react app folder

`cd my-app`

Replace the `my-app` src folder with the one included in the repository

Start the app

`npm start`


## Oracle Database Script

The script for the oracle database it's in the database_script folder. This script
can be run by sqldeveloper or sql terminal utility.










