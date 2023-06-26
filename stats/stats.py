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
        'Rebounds TOT': [],
        'Rebounds OR' : [],
        'Rebounds DR' : [],
        'Blocks': [],
        'Three Points Made': [],
        'Three Points Attempts': [],
        'Three Points Percentage': [],
        'Two Points Made': [],
        'Two Points Attempts': [],
        'Two Points Percentage': [],
        'FG Made':[],
        'FG Attempts':[],
        'FG Percentage':[],
        'Fouls PF' :[],
        'Fouls FD':[],
        'Free Throws Made':[],
        'Free Throws Attempts':[],
        'Free Throws Percentage':[],
        'TO':[],
        'ST':[],
        'Plus or Minus':[]

    }

    # Step 6: Iterate over the DataFrame to calculate rankings for each category
    for index, row in df.iterrows():
        player_name = row['Player']
        points = row['PTS']
        assists = row['AS']
        rebounds_tot = row['Rebounds TOT']
        rebounds_or = row['Rebounds OR']
        rebounds_dr = row['Rebounds DR']
        blocks = row['BS']
        three_points_made = row['Three Points Made']
        three_points_attempts = row['Three Points Attempts']
        three_points_percentage = row['Three Points Percentage']
        two_points_made = row['Two Points Made']
        two_points_attempts = row['Two Points Attempts']
        two_points_percentage = row['Two Points Percentage']
        field_goals_made = row['FG Made']
        field_goals_attempts = row['FG Attempts']
        field_goals_percentage = row['FG Percentage']
        fouls_pf = row['Fouls PF']
        fouls_fd = row['Fouls FD']
        free_throws_made = row['Free Throws Made']
        free_throws_attempts = row['Free Throws Attempts']
        free_throws_percentage = row['Free Throws Percentage']
        to = row['TO']
        st = row['ST']
        plus_or_minus = row['Plus or Minus']

        # Update rankings dictionary for each category
        rankings['Player'].append(player_name)
        rankings['Points'].append(points)
        rankings['Assists'].append(assists)
        rankings['Rebounds TOT'].append(rebounds_tot)
        rankings['Rebounds OR'].append(rebounds_or)
        rankings['Rebounds DR'].append(rebounds_dr)
        rankings['Blocks'].append(blocks)
        rankings['Three Points Made'].append(three_points_made)
        rankings['Three Points Attempts'].append(three_points_attempts)
        rankings['Three Points Percentage'].append(three_points_percentage)
        rankings['Two Points Made'].append(two_points_made)
        rankings['Two Points Attempts'].append(two_points_attempts)
        rankings['Two Points Percentage'].append(two_points_percentage)
        rankings['FG Made'].append(field_goals_made)
        rankings['FG Attempts'].append(field_goals_attempts)
        rankings['FG Percentage'].append(field_goals_percentage)
        rankings['Fouls PF'].append(fouls_pf)
        rankings['Fouls FD'].append(fouls_fd)
        rankings['Free Throws Made'].append(free_throws_made)
        rankings['Free Throws Attempts'].append(free_throws_attempts)
        rankings['Free Throws Percentage'].append(free_throws_percentage)
        rankings['TO'].append(to)
        rankings['ST'].append(st)
        rankings['Plus or Minus'].append(plus_or_minus)

    # Step 7: Create a DataFrame for the rankings
    rankings_df = pd.DataFrame(rankings)

    # Step 8: Sort the rankings in descending order by each category
    rankings_df.sort_values(by='Points', ascending=False, inplace=True)
    rankings_df['Points Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Assists', ascending=False, inplace=True)
    rankings_df['Assists Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Rebounds TOT', ascending=False, inplace=True)
    rankings_df['Rebounds TOT Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Rebounds OR', ascending=False, inplace=True)
    rankings_df['Rebounds OR Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Blocks', ascending=False, inplace=True)
    rankings_df['Blocks Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Three Points Made', ascending=False, inplace=True)
    rankings_df['Three Points Made Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Three Points Attempts', ascending=False, inplace=True)
    rankings_df['Three Points Attempts Rank'] = range(1, len(rankings_df) + 1)
    
    rankings_df.sort_values(by='Three Points Percentage', ascending=False, inplace=True)
    rankings_df['Three Points Percentage Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Two Points Made', ascending=False, inplace=True)
    rankings_df['Two Points Made Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Two Points Attempts', ascending=False, inplace=True)
    rankings_df['Two Points Attempts Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Two Points Attempts', ascending=False, inplace=True)
    rankings_df['Two Points Attempts Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='FG Made', ascending=False, inplace=True)
    rankings_df['FG Made Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='FG Attempts', ascending=False, inplace=True)
    rankings_df['FG Attempts Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='FG Percentage', ascending=False, inplace=True)
    rankings_df['FG Percentage Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Fouls PF', ascending=False, inplace=True)
    rankings_df['Fouls PF Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Fouls FD', ascending=False, inplace=True)
    rankings_df['Fouls FD Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Free Throws Made', ascending=False, inplace=True)
    rankings_df['Free Throws Made Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Free Throws Attempts', ascending=False, inplace=True)
    rankings_df['Free Throws Attempts Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Free Throws Percentage', ascending=False, inplace=True)
    rankings_df['Free Throws Percentage Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='TO', ascending=False, inplace=True)
    rankings_df['TO Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='ST', ascending=False, inplace=True)
    rankings_df['ST Rank'] = range(1, len(rankings_df) + 1)

    rankings_df.sort_values(by='Plus or Minus', ascending=False, inplace=True)
    rankings_df['Plus or Minus Rank'] = range(1, len(rankings_df) + 1)


    # Step 9: Save the DataFrame to a CSV file
  

    rankings_df.to_csv(f'finals/{team_name}{game_date}rankings.csv', index=False)





    

#def map_csv_to_postgres(csv_file, team_name, game_date):
    # # Step 1: Read the CSV file using pandas
    # df = pd.read_csv(csv_file)

    # # Step 2: Create a connection to the PostgreSQL database
    # engine = create_engine('postgresql://postgres:1234567890@localhost/nukta-box')

    # # Step 3: Define the table name based on team name and game date
    # table_name = f'{team_name}{game_date}rankings'

    # # Step 4: Create the table if it doesn't exist
    # df.head(0).to_sql(table_name, con=engine, if_exists='replace', index=False)

    # # Step 5: Insert the data into the table
    # with engine.connect() as connection:
    #     df.to_sql(table_name, con=connection, if_exists='append', index=False)

    # print(f"The data has been mapped to the '{table_name}' table in the PostgreSQL database.")    
