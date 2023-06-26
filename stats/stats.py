import pandas as pd
from sqlalchemy import create_engine
import os 






def calculate_rankings(csv_file, team_name, game_date):
    # Step 3: Read the CSV file using pandas
    df = pd.read_csv(csv_file)

    # Step 4: Filter out the row containing the totals
    df = df[df['Player'] != 'Totals']

    # Step 5: Create dictionaries to store rankings for each category
    rankings = {
        'Player': [],
        'Points': [],
        'Assists': [],
        'Rebounds': [],
        'Blocks': [],
        'Three Points': [],
        'Two Points': []
    }

    # Step 6: Iterate over the DataFrame to calculate rankings for each category
    for index, row in df.iterrows():
        player_name = row['Player']
        points = row['PTS']
        assists = row['AS']
        rebounds = row['Rebounds TOT']
        blocks = row['BS']
        three_points = row['three points made']
        two_points = row['two points made']

        # Update rankings dictionary for each category
        rankings['Player'].append(player_name)
        rankings['Points'].append(points)
        rankings['Assists'].append(assists)
        rankings['Rebounds'].append(rebounds)
        rankings['Blocks'].append(blocks)
        rankings['Three Points'].append(three_points)
        rankings['Two Points'].append(two_points)

    # Step 7: Create a DataFrame for the rankings
    rankings_df = pd.DataFrame(rankings)

    # Step 8: Sort the rankings in descending order by each category
    rankings_df.sort_values(by='Points', ascending=False, inplace=True)
    rankings_df['Points Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Assists', ascending=False, inplace=True)
    rankings_df['Assists Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Rebounds', ascending=False, inplace=True)
    rankings_df['Rebounds Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Blocks', ascending=False, inplace=True)
    rankings_df['Blocks Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Three Points', ascending=False, inplace=True)
    rankings_df['Three Points Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Two Points', ascending=False, inplace=True)
    rankings_df['Two Points Rank'] = range(1, len(rankings_df) + 1)

    # Step 9: Save the DataFrame to a CSV file
  

    rankings_df.to_csv(f'finals/{team_name}{game_date}rankings.csv', index=False)

def map_csv_to_postgres(csv_file, team_name, game_date):
    # Step 1: Read the CSV file using pandas
    df = pd.read_csv(csv_file)

    # Step 2: Create a connection to the PostgreSQL database
    engine = create_engine('postgresql://postgres:1234567890@localhost/nukta-box')

    # Step 3: Define the table name based on team name and game date
    table_name = f'{team_name}{game_date}rankings'

    # Step 4: Create the table if it doesn't exist
    df.head(0).to_sql(table_name, con=engine, if_exists='replace', index=False)

    # Step 5: Insert the data into the table
    with engine.connect() as connection:
        df.to_sql(table_name, con=connection, if_exists='append', index=False)

    print(f"The data has been mapped to the '{table_name}' table in the PostgreSQL database.")    
