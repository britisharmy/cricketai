CREATE TABLE cricket_performance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_name VARCHAR(50),
    runs_scored INT,
    balls_faced INT,
    strike_rate FLOAT,
    batting_average FLOAT,
    boundaries INT,
    innings_played INT,
    balls_bowled INT,
    wickets_taken INT,
    bowling_economy FLOAT,
    bowling_average FLOAT,
    maiden_overs INT,
    dot_balls INT,
    catches_taken INT,
    stumpings INT,
    performance_category ENUM('Runs_Scored', 'Balls_Faced', 'Strike_Rate', 'Batting_Average', 'Boundaries', 'Innings_Played', 'Balls_Bowled', 'Wickets_Taken', 'Bowling_Economy', 'Bowling_Average', 'Maiden_Overs', 'Dot_Balls', 'Catches_Taken', 'Stumpings')
);
