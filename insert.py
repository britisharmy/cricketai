import mysql.connector
from faker import Faker
import random

# Connect to MySQL
mydb = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)

mycursor = mydb.cursor()

# List of predefined Indian names to be repeated
indian_names = ["Rohit Sharma", "Virat Kohli", "MS Dhoni", "Jasprit Bumrah", "Ravichandran Ashwin", "Hardik Pandya"]

# Insert 400,000 records
for _ in range(400000):
    player_name = random.choice(indian_names)
    runs_scored = random.randint(0, 200)
    balls_faced = random.randint(0, 300)
    strike_rate = round(random.uniform(50, 200), 2)
    # ... assign other random values for the parameters

    # Selecting a random performance category for the enum field
    performance_categories = ['Runs_Scored', 'Balls_Faced', 'Strike_Rate', 'Batting_Average', 'Boundaries', 'Innings_Played',
                              'Balls_Bowled', 'Wickets_Taken', 'Bowling_Economy', 'Bowling_Average', 'Maiden_Overs',
                              'Dot_Balls', 'Catches_Taken', 'Stumpings']
    performance_category = random.choice(performance_categories)

    # SQL query to insert data
    sql = "INSERT INTO cricket_performance (player_name, runs_scored, balls_faced, strike_rate, performance_category) VALUES (%s, %s, %s, %s, %s)"
    val = (player_name, runs_scored, balls_faced, strike_rate, performance_category)

    mycursor.execute(sql, val)

# Commit the changes and close connection
mydb.commit()
mydb.close()
