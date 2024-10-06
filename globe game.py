import pygame
import sys
import mysql.connector

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((900, 450))
pygame.display.set_caption("Neowise")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red=(255,255,255)
blue = (0, 0, 255)
green = (0, 255, 0)
gray = (169, 169, 169)
bright_green = (0, 255, 0)
dim_green = (100, 255, 100)

# Font setup
font = pygame.font.Font(None, 32)
title_font = pygame.font.Font(None, 48)

# Login page input box setup
input_box_username = pygame.Rect(370, 150, 200, 32)
input_box_password = pygame.Rect(370, 200, 200, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color_username = color_inactive
color_password = color_inactive
active_username = False
active_password = False
username = ''
password = ''
login_done = False
signup_mode = False

# Sign-up page input boxes
input_box_name = pygame.Rect(370, 100, 200, 32)
input_box_age = pygame.Rect(370, 150, 200, 32)
input_box_email = pygame.Rect(370, 200, 200, 32)
input_box_signup_password = pygame.Rect(370, 250, 200, 32)
name = ''
age = ''
email = ''
signup_password = ''
active_name = False
active_age = False
active_email = False
active_signup_password = False

# Button setup
button_login = pygame.Rect(350, 260, 90, 40)
button_signup = pygame.Rect(460, 260, 90, 40)
button_submit_signup = pygame.Rect(350, 300, 200, 40)

# Load background for next screen
background = pygame.image.load('space.jpeg')

# Level setup
level_1 = pygame.Rect(300, 150, 150, 40)
level_2 = pygame.Rect(300, 220, 150, 40)
level_3 = pygame.Rect(300, 290, 150, 40)
level_4 = pygame.Rect(300, 360, 150, 40)

enabled_levels = [1]  # Only levels 1 and 2 are enabled, level 3 is locked

# Question setup
questions = {
    1: [
        {"question": "What does the GLOBE Program focus on?", 
         "options": ["Scientific literacy", "Cultural studies", "Sports education", "Political science"], 
         "correct": 1},
        {"question": "Which of the following is NOT a GLOBE protocol?", 
         "options": ["Soil Moisture", "Air Quality", "Space Exploration", "Water Temperature"], 
         "correct": 3},
        {"question": "If you notice unusual weather patterns in your area, what should you do?", 
         "options": ["Ignore it", "Report it to GLOBE", "Move to another area", "Post about it on social media"], 
         "correct": 2},
        {"question": "What can you measure using the GLOBE Hydrology protocol?", 
         "options": ["Soil erosion", "Water temperature", "Wildlife populations", "Air pressure"], 
         "correct": 2},
        {"question": "Which GLOBE protocol involves observing clouds?", 
         "options": ["Soil", "Atmosphere", "Water", "Biosphere"], 
         "correct": 2},
        {"question": "What is one benefit of participating in the GLOBE Program?", 
         "options": ["Learning to cook", "Developing scientific skills", "Traveling abroad", "Winning prizes"], 
         "correct": 2},
    ],
    2: [
        {"question": "What should you do if you see litter in a water body?", 
         "options": ["Leave it", "Report it to local authorities", "Take a picture", "Blame others"], 
         "correct": 2},
        {"question": "Which of the following contributes to urban heat islands?", 
         "options": ["Vegetation", "High buildings and asphalt", "Water bodies", "Open fields"], 
         "correct": 2},
        {"question": "What is the primary focus of the GLOBE Soil protocol?", 
         "options": ["Measuring air quality", "Observing plant growth", "Analyzing soil composition", "Tracking animal behavior"], 
         "correct": 3},
        {"question": "How can excessive urbanization affect local water bodies?", 
         "options": ["Improve water quality", "Increase flooding risk", "Decrease pollution", "Enhance biodiversity"], 
         "correct": 2},
        {"question": "What is one way to reduce water pollution?", 
         "options": ["Use more plastic", "Properly dispose of chemicals", "Ignore regulations", "Increase industrial waste"], 
         "correct": 2},
        {"question": "If you experience a drought, what is a recommended action?", 
         "options": ["Waste water", "Plant drought-resistant plants", "Use more water", "Ignore the situation"], 
         "correct": 2},
    ],
    3: [
        {"question": "What is a key method for collecting GLOBE data?", 
         "options": ["Guessing", "Direct measurement", "Social media posts", "Surveys"], 
         "correct": 2},
        {"question": "Which instrument is commonly used in the GLOBE Atmosphere protocol?", 
         "options": ["Thermometer", "Ruler", "Stopwatch", "Scale"], 
         "correct": 1},
        {"question": "What should you do if you collect data that seems incorrect?", 
         "options": ["Ignore it", "Recheck your methods", "Change the data", "Tell others it’s right"], 
         "correct": 2},
        {"question": "Which GLOBE protocol includes measuring the pH of water?", 
         "options": ["Hydrology", "Atmosphere", "Land Cover", "Soil"], 
         "correct": 1},
        {"question": "Why is it important to share collected data with GLOBE?", 
         "options": ["To compete with others", "To contribute to global understanding", "To get recognition", "To hoard information"], 
         "correct": 2},
        {"question": "What is the significance of long-term data collection?", 
         "options": ["It doesn't matter", "It helps identify trends", "It's a waste of time", "Only short-term data is useful"], 
         "correct": 2},
    ],
    4: [
        {"question": "If a community is facing flooding, what is a proactive step?", 
         "options": ["Build more houses", "Implement better drainage systems", "Ignore the issue", "Wait for help"], 
         "correct": 2},
        {"question": "What can individuals do to combat climate change?", 
         "options": ["Increase energy consumption", "Reduce waste and recycle", "Drive more", "Avoid public transport"], 
         "correct": 2},
        {"question": "In the event of a wildfire, what should you prioritize?", 
         "options": ["Take photos", "Evacuate to safety", "Stay to watch", "Ignore warnings"], 
         "correct": 2},
        {"question": "What is one way to engage the community in environmental issues?", 
         "options": ["Host clean-up events", "Keep it a secret", "Avoid discussing it", "Create more waste"], 
         "correct": 1},
        {"question": "Which of the following is an effect of global warming?", 
         "options": ["Cooler temperatures", "Rising sea levels", "Increased snowfall", "None of the above"], 
         "correct": 2},
        {"question": "If your community has a pollution problem, who should you contact?", 
         "options": ["The local government", "Your friends", "No one", "The media only"], 
         "correct": 1},
    ]
}



def display_levels():
    screen.fill(white)

    # Render levels
    pygame.draw.rect(screen, bright_green if 1 in enabled_levels else dim_green, level_1)
    pygame.draw.rect(screen, bright_green if 2 in enabled_levels else dim_green, level_2)
    pygame.draw.rect(screen, bright_green if 3 in enabled_levels else dim_green, level_3)
    pygame.draw.rect(screen, bright_green if 4 in enabled_levels else dim_green, level_4)
    
    screen.blit(font.render("Level 1", True, white), (level_1.x + 40, level_1.y + 5))
    screen.blit(font.render("Level 2", True, white), (level_2.x + 40, level_2.y + 5))
    screen.blit(font.render("Level 3", True, white), (level_3.x + 40, level_3.y + 5))
    screen.blit(font.render("Level 4", True, white), (level_4.x + 40, level_4.y + 5))

    pygame.display.update()

def display_question(level, question):
    screen.fill( white )
    screen.blit(background, (0, 0))

    # Render question
    screen.blit(font.render(question["question"], True, black), (100, 100))

    # Render options
    for i, option in enumerate(question["options"]):
        option_rect = pygame.Rect(100, 150 + i * 60, 600, 50)
        pygame.draw.rect(screen, green, option_rect, 2)
        screen.blit(font.render(option, True, black), (option_rect.x + 10, option_rect.y + 10))

    pygame.display.update()

def play_level(level):
    marks = 0
    for question in questions[level]:
        display_question(level, question)
        waiting_for_answer = True
        while waiting_for_answer:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    maxv=max(enabled_levels)
                    cur.execute(f"UPDATE game SET Level = {maxv} WHERE Username = '{username}'")
                    conn.commit()
                    cur.close()
                    conn.close()
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, option in enumerate(question["options"]):
                        option_rect = pygame.Rect(100, 150 + i * 60, 600, 50)
                        if option_rect.collidepoint(event.pos):
                            if i + 1 == question["correct"]:
                                marks += 1
                                print("Correct answer!")
                            else:
                                print("Incorrect answer.")
                            waiting_for_answer = False
        screen.fill(white)
        screen.blit(background, (0, 0))
        screen.blit(font.render(f"Marks: {marks}", True, black), (100, 100))
        pygame.display.update()
        pygame.time.wait(1000)
    if marks >= 3:
        print(f"Level {level} passed with {marks} marks")
        result_message = f"Level {level} passed with {marks} marks"
        if level == 1:
            enabled_levels.append(2)
        elif level == 2:
            enabled_levels.append(3)
        elif level == 3:
            enabled_levels.append(4)
    else:
        print(f"Level {level} failed with {marks} marks")
        result_message = f"Level {level} failed with {marks} marks"
    
    screen.blit(font.render(result_message, True, black), (100, 200))
    pygame.display.update()
    pygame.time.wait(3000)

# MySQL database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="game"
)
cur = conn.cursor()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            maxv=max(enabled_levels)
            cur.execute(f"UPDATE game SET Level = {maxv} WHERE Username = '{username}'")
            conn.commit()
            cur.close()
            conn.close()
            pygame.quit()
            exit()

        if not login_done:
            # Handle sign-up input events
            if signup_mode:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box_name.collidepoint(event.pos):
                        active_name = not active_name
                    else:
                        active_name = False
                    if input_box_age.collidepoint(event.pos):
                        active_age = not active_age
                    else:
                        active_age = False
                    if input_box_email.collidepoint(event.pos):
                        active_email = not active_email
                    else:
                        active_email = False
                    if input_box_signup_password.collidepoint(event.pos):
                        active_signup_password = not active_signup_password
                    else:
                        active_signup_password = False

                    # Submit sign-up information
                    if button_submit_signup.collidepoint(event.pos):
                        print(f"Sign-Up Info: Name={name}, Age={age}, Email={email}, Password={signup_password}")
                        cur.execute(f"INSERT INTO game (Username, Password, Age, Email, Level) VALUES ('{name}', '{signup_password}', {age}, '{email}', 1)")
                        conn.commit()
                        signup_mode = False  # Go back to login after signing up
                        login_done = True  # Move to the next stage (background)

                # Handle text input for sign-up
                if event.type == pygame.KEYDOWN:
                    if active_name:
                        if event.key == pygame.K_BACKSPACE:
                            name = name[:-1]
                        else:
                            name += event.unicode
                    if active_age:
                        if event.key == pygame.K_BACKSPACE:
                            age = age[:-1]
                        else:
                            age += event.unicode
                    if active_email:
                        if event.key == pygame.K_BACKSPACE:
                            email = email[:-1]
                        else:
                            email += event.unicode
                    if active_signup_password:
                        if event.key == pygame.K_BACKSPACE:
                            signup_password = signup_password[:-1]
                        else:
                            signup_password += event.unicode

            else:
                # Handle login input events
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box_username.collidepoint(event.pos):
                        active_username = not active_username
                    else:
                        active_username = False
                    if input_box_password.collidepoint(event.pos):
                        active_password = not active_password
                    else:
                        active_password = False

                    color_username = color_active if active_username else color_inactive
                    color_password = color_active if active_password else color_inactive

                    # Check if the login or signup buttons were clicked
                    if button_login.collidepoint(event.pos):
                        print(f"Login Info: Username={username}, Password={password}")
                        cur.execute(f"SELECT * FROM game WHERE Username='{username}' AND Password='{password}'")
                        result = cur.fetchone()
                        if result:
                           lvl=result[4]
                           enabled_levels = [i for i in range(1, lvl + 1)]
                           message = "Login successful"
                           login_done = True  # Move to the background after login
                           screen.blit(font.render(message, True, black), (350, 350))
                           pygame.display.update()  # Update the display to make the message visible
                           pygame.time.wait(2000)  # Wait for 2 seconds before continuing
                        else:
                           message = "Invalid details"
                           screen.blit(font.render(message, True, black), (350, 350))
                           pygame.display.update()  # Update the display to make the message visible
                           pygame.time.wait(2000)  # Wait for 2 seconds before continuing
                        
                    elif button_signup.collidepoint(event.pos):
                        signup_mode = True  # Switch to sign-up mode

                # Handle text input for login
                if event.type == pygame.KEYDOWN:
                    if active_username:
                        if event.key == pygame.K_BACKSPACE:
                            username = username[:-1]
                        else:
                            username += event.unicode
                    if active_password:
                        if event.key == pygame.K_BACKSPACE:
                            password = password[:-1]
                        else:
                            password += event.unicode

            # Render login or sign-up screen based on mode
            if signup_mode:
                screen.fill(white)

                # Render title for sign-up
                title_surface = title_font.render("Sign Up", True, black)
                screen.blit(title_surface, (350, 50))

                # Render labels for sign-up fields
                label_name = font.render("Username", True, black)
                label_age = font.render("Age", True, black)
                label_email = font.render("Email", True, black)
                label_signup_password = font.render("Password", True, black)

                screen.blit(label_name, (250, 105))
                screen.blit(label_age, (250, 155))
                screen.blit(label_email, (250, 205))
                screen.blit(label_signup_password, (250, 255))

                # Render input boxes for sign-up
                for box, text in [(input_box_name, name), (input_box_age, age), (input_box_email, email), (input_box_signup_password, signup_password)]:
                    pygame.draw.rect(screen, color_active if box.collidepoint(pygame.mouse.get_pos()) else color_inactive, box, 2)
                    screen.blit(font.render(text, True, black), (box.x + 5, box.y + 5))

                # Render "Submit" button for sign-up
                pygame.draw.rect(screen, green, button_submit_signup)
                screen.blit(font.render("Submit", True, white), (button_submit_signup.x + 40, button_submit_signup.y + 10))

            else:
                # Render login screen
                screen.fill(white)

                # Render title
                title_surface = title_font.render("Login", True, black)
                screen.blit(title_surface, (350, 80))

                # Render labels
                label_username = font.render("Username", True, black)
                label_password = font.render("Password", True, black)
                screen.blit(label_username, (250, 155))  # Label for username
                screen.blit(label_password, (250, 205))  # Label for password

                # Render text input boxes
                pygame.draw.rect(screen, color_username, input_box_username, 2)
                pygame.draw.rect(screen, color_password, input_box_password, 2)
                screen.blit(font.render(username, True, black), (input_box_username.x + 5, input_box_username.y + 5))
                screen.blit(font.render(password, True, black), (input_box_password.x + 5, input_box_password.y + 5))

                # Render login and signup buttons
                pygame.draw.rect(screen, blue, button_login)
                pygame.draw.rect(screen, green, button_signup)
                screen.blit(font.render("Login", True, white), (button_login.x + 10, button_login.y + 10))
                screen.blit(font.render("Sign Up", True, white), (button_signup.x + 5, button_signup.y + 10))

            pygame.display.update()

        else:
            # Handle level selection click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if level_1.collidepoint(event.pos) and 1 in enabled_levels:
                    play_level(1)
                if level_2.collidepoint(event.pos) and 2 in enabled_levels:
                    play_level(2)
                if level_3.collidepoint(event.pos) and 3 in enabled_levels:
                    play_level(3)
                if level_4.collidepoint(event.pos) and 4 in enabled_levels:
                    play_level(4)

            display_levels()