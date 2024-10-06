# NEOWISE-GLOBE-PROTOCOL-GAME
Neowise GLOBE PROTOCOL GAME
Neowise is an interactive educational game designed to raise awareness of environmental science. Players answer questions based on the GLOBE Program protocols to progress through levels, learning more about sustainability and environmental care.

Features
Login and Sign-up:

Players can log in using their username and password or sign up with basic details (username, age, email, and password).
Login progress is stored in a MySQL database.
Four Levels:

Levels are unlocked as the player progresses, based on their score in each level.
Each level contains multiple-choice questions designed to teach players about the environment, with topics such as the GLOBE Program, urbanization, and pollution prevention.
MySQL Integration:

Player information and game progress are stored in a MySQL database for persistence.
Requirements
Python 3.12.7
Pygame: Python library for game development.
MySQL: Used to store login credentials and progress etc.
Install the necessary Python libraries using the following:

bash
Copy code
pip install pygame mysql.connector
Setup
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/neowise-game.git
cd neowise-game
Set up the MySQL database:

Create a database named game.
Run the following SQL command to create the required table:
sql
Copy code
CREATE TABLE game (
    Username VARCHAR(50),
    Password VARCHAR(50),
    Age INT,
    Email VARCHAR(100),
    Level INT
);
Replace the database credentials in the code to match your MySQL configuration:

python
Copy code
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="game"
)
Run the game:

bash
Copy code
python neowise_game.py
How to Play
Login: Enter your username and password to continue your progress.
Sign-up: If you're a new player, sign up by providing your name, age, email, and password.
Answer Questions: Progress through the levels by answering multiple-choice questions correctly. You need to score at least 3 correct answers to pass each level and unlock the next.
Project Structure
bash
Copy code
.
├── neowise_game.py      # Main game logic
├── space.jpeg           # Background image used in the game
└── README.md            # This file
Future Scope
Add more environmental topics and levels.
Implement leaderboards to encourage competition.
Integrate additional data collection mechanisms for tracking user progress.
