# NEOWISE GLOBE PROTOCOL GAME

Neowise is an interactive educational game designed to raise awareness of environmental science. Players answer questions based on the GLOBE Program protocols to progress through levels, learning more about sustainability and environmental care.

## Features

-Login and Sign-up
-Players can log in using their username and password or sign up with basic details (username, age, email, and password).
-Login progress is stored in a MySQL database.
-Four Levels:

    - Levels are unlocked as the player progresses, based on their score in each level.
    - Each level contains multiple-choice questions designed to teach players about the environment, with topics such as the GLOBE Program, urbanization, and pollution prevention.
- MySQL Integration
- Player information and game progress are stored in a MySQL database for persistence.
- Interactive game on environmental topics.
- Login system to save user progress.
- Scoring system to track user achievements.
- Built with **Python Pygame** for the game interface.
- Utilizes **MySQL** for storing user login credentials.

## Installation

### Requirements

- **Python 3.12.7**
- **Pygame:** A Python library for game development.
- **MySQL:** Used to store login credentials and progress.

Install the necessary Python libraries using the following:

```bash
pip install pygame mysql.connector
