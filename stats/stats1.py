import pandas as pd

# Step 3: Read the CSV file using pandas
df = pd.read_csv('boxscorehome.csv')

# Step 4: Filter out the row containing the totals
df = df[df['Player'] != 'Totals']

# Step 5: Iterate over the DataFrame to display player stats
for index, row in df.iterrows():
    player_name = row['Player']
    player_stats = {
        'Player': player_name,
        'Total Points': row['PTS'],
        'Two-Point Percentage': row['two points percentage'],
        'Two-Point Made': row['two points made'],
        'Two-Point Attempts': row['two points attempts'],
        'Three-Point Percentage': row['three points percentage'],
        'Three-Point Made': row['three points made'],
        'Three-Point Attempts': row['three points attempts'],
        'FG Percentage': row['FG percentage'],
        'FG Made': row['FG made'],
        'FG Attempts': row['FG attempts'],
        'Fouls PF': row['Fouls PF'],
        'Fouls FD': row['Fouls FD'],
        'Free Throws Percentage': row['Free Throws Percentage'],
        'Free Throws Made': row['Free Throws Made'],
        'Free Throws Attempts': row['Free Throws Attempts'],
        'Rebounds OR': row['Rebounds OR'],
        'Rebounds DR': row['Rebounds DR'],
        'Rebounds TOT': row['Rebounds TOT'],
        'Min': row['Min'],
        'AS': row['AS'],
        'TO': row['TO'],
        'ST': row['ST'],
        'BS': row['BS'],
        'plus or minus': row['plus or minus']
    }

    # Step 6: Display player stats
    print(player_stats)
    print()