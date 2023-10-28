import mysql.connector
from faker import Faker
import random
import concurrent.futures

# Function to insert data
def insert_data(player_names):
    mydb = mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password",
        database="your_database"
    )

    mycursor = mydb.cursor()

    for _ in range(100000):  # Insert 100,000 records per thread
        player_name = random.choice(player_names)
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

    mydb.commit()
    mydb.close()

if __name__ == "__main__":
    # List of predefined Indian names to be repeated
    indian_names = ["Rohit Sharma", "Virat Kohli", "MS Dhoni", "Jasprit Bumrah", "Ravichandran Ashwin", "Hardik Pandya"]

    # Dividing data insertion task among multiple threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:  # Change max_workers based on your system
        player_name_chunks = [indian_names[i:i + 2] for i in range(0, len(indian_names), 2)]
        executor.map(insert_data, player_name_chunks)
