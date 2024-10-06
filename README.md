# PROBLEM STATEMENT
Learning about science can be a fun experience! Games that focus on science and environmental issues can create opportunities for players to develop their interests and gain knowledge while engaging with each other in a fun way. Your challenge is to create a game that integrates Global Learning and Observations to Benefit the Environment (GLOBE) Program protocols to help players understand the world around them, develop awareness of one or more local or global environmental topics, investigate their local community using GLOBE protocols, or learn scientific principles.
# SOLUTION:

# NEOWISE GLOBE PROTOCOL GAME

Neowise is an interactive educational game designed to raise awareness of environmental science. Players answer questions based on the GLOBE Program protocols to progress through levels, learning more about sustainability and environmental care.

## Features

- Login and Sign-up
- Players can log in using their username and password or sign up with basic details.
- Login progress is stored in a MySQL database.
- Four Levels:
    - Levels are unlocked as the player progresses, based on their score in each level.
    - Each level contains multiple-choice questions designed to teach players about the environment, with topics such as the GLOBE Program, urbanization, and pollution prevention.
- MySQL Integration
- Player information and game progress are stored in a MySQL database for persistence.
- Interactive game on environmental topics.
- Login system to save user progress.
- Scoring system to track user achievements.
- Built with **Python Pygame** for the game interface.
- Utilizes **MySQL** for storing user login credentials.


### Requirements

- **Python 3.12.7**
- **Pygame:** A Python library for game development.
- **MySQL:** Used to store login credentials and progress.
- Copy the image to the same directory
'''bash
Install the necessary Python libraries using the following:

## Installation

## To install Python Modules
- pip install pygame mysql.connector

## MySQL setup:
  - install mysql
  - create database game;
  - CREATE TABLE users (Username VARCHAR(255) , Password VARCHAR(255) , Age int , Email varchar(50) , level int default 1);
  - conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="game"
) change it according to your details in the program

## Game Instructions
 - Start the game and log in using your credentials.
 - Follow the on-screen instructions to navigate through various environmental science challenges.
 - Accumulate points by completing tasks that raise awareness about environmental conservation.
