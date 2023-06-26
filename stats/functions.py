import pandas as pd

import os


    

def two_pointer(file_path, column_name):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Clean and normalize the column names
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces from column names

    # Find the closest matching column name
    matching_columns = [col for col in df.columns if column_name.lower() in col.lower()]
    if len(matching_columns) > 0:
        column_name = matching_columns[0]

    # Extract the column values and store them in a dictionary
    column_values = df[column_name].tolist()
    column_dict = {column_name: column_values}

    # Create a new DataFrame from the dictionary
    df_new = pd.DataFrame(column_dict)

    # Split the 'Field Goals' column into two temporary columns
    df_new[['2P_temp', '2P (%)']] = df_new[column_name].str.split(expand=True)

    # Further split the 'FG_temp' column into 'FG (M)' and 'FG (A)'
    df_new[['2P (M)', '2P (A)']] = df_new['2P_temp'].str.split('/', expand=True)

    # Drop the temporary columns
    df_new = df_new.drop(['2 Points', '2P_temp'], axis=1)

    # Drop rows with NaN values
    df_new = df_new.dropna()

    # Reset the index of the DataFrame
    df_new = df_new.reset_index(drop=True)

    return df_new

def three_pointer(file_path, column_name):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Clean and normalize the column names
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces from column names

    # Find the closest matching column name
    matching_columns = [col for col in df.columns if column_name.lower() in col.lower()]
    if len(matching_columns) > 0:
        column_name = matching_columns[0]

    # Extract the column values and store them in a dictionary
    column_values = df[column_name].tolist()
    column_dict = {column_name: column_values}

    # Create a new DataFrame from the dictionary
    df_new = pd.DataFrame(column_dict)

    # Split the column into two temporary columns
    df_new[[f'{column_name}_temp', f'{column_name} (%)']] = df_new[column_name].str.split(expand=True)

    # Further split the temporary column into '(M)' and '(A)'
    df_new[[f'{column_name} (M)', f'{column_name} (A)']] = df_new[f'{column_name}_temp'].str.split('/', expand=True)

    # Drop the temporary columns
    df_new = df_new.drop([column_name, f'{column_name}_temp'], axis=1)

    # Drop rows with NaN values
    df_new = df_new.dropna()

    # Reset the index of the DataFrame
    df_new = df_new.reset_index(drop=True)

    return df_new


def field_goals(file_path, column_name):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Clean and normalize the column names
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces from column names

    # Find the closest matching column name
    matching_columns = [col for col in df.columns if column_name.lower() in col.lower()]
    if len(matching_columns) > 0:
        column_name = matching_columns[0]

    # Extract the column values and store them in a dictionary
    column_values = df[column_name].tolist()
    column_dict = {column_name: column_values}

    # Create a new DataFrame from the dictionary
    df_new = pd.DataFrame(column_dict)

    # Split the 'Field Goals' column into two temporary columns
    df_new[['FG_temp', 'FG (%)']] = df_new[column_name].str.split(expand=True)

    # Further split the 'FG_temp' column into 'FG (M)' and 'FG (A)'
    df_new[['FG (M)', 'FG (A)']] = df_new['FG_temp'].str.split('/', expand=True)

    # Drop the temporary columns
    df_new = df_new.drop([column_name, 'FG_temp'], axis=1)

    # Drop rows with NaN values
    df_new = df_new.dropna()

    # Reset the index of the DataFrame
    df_new = df_new.reset_index(drop=True)

    return df_new

def fouls(file_path, column_name):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Clean and normalize the column names
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces from column names

    # Find the closest matching column name
    matching_columns = [col for col in df.columns if column_name.lower() in col.lower()]
    if len(matching_columns) > 0:
        column_name = matching_columns[0]

    # Extract the column values and store them in a dictionary
    column_values = df[column_name].tolist()
    column_dict = {column_name: column_values}

    # Create a new DataFrame from the dictionary
    df_new = pd.DataFrame(column_dict)

    # Split the column into two temporary columns
    df_new[['Fouls (PF)', 'Fouls (FD)']] = df_new[column_name].str.split(expand=True)

    # Drop the original column
    df_new = df_new.drop(column_name, axis=1)

    # Drop rows with NaN values
    df_new = df_new.dropna()

    # Reset the index of the DataFrame
    df_new = df_new.reset_index(drop=True)

    return df_new

def free_throws(file_path, column_name):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Clean and normalize the column names
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces from column names

    # Find the closest matching column name
    matching_columns = [col for col in df.columns if column_name.lower() in col.lower()]
    if len(matching_columns) > 0:
        column_name = matching_columns[0]

    # Extract the column values and store them in a dictionary
    column_values = df[column_name].tolist()
    column_dict = {column_name: column_values}

    # Create a new DataFrame from the dictionary
    df_new = pd.DataFrame(column_dict)

    # Split the column into two temporary columns
    df_new[['FT_temp', 'FT (%)']] = df_new[column_name].str.split(expand=True)

    # Further split the 'FT_temp' column into 'FT (M)' and 'FT (A)'
    df_new[['FT (M)', 'FT (A)']] = df_new['FT_temp'].str.split('/', expand=True)

    # Drop the temporary columns
    df_new = df_new.drop([column_name, 'FT_temp'], axis=1)

    # Drop rows with NaN values
    df_new = df_new.dropna()

    # Reset the index of the DataFrame
    df_new = df_new.reset_index(drop=True)

    return df_new

def reb(file_path, column_name):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Clean and normalize the column names
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces from column names

    # Find the closest matching column name
    matching_columns = [col for col in df.columns if column_name.lower() in col.lower()]
    if len(matching_columns) > 0:
        column_name = matching_columns[0]

    # Extract the column values and store them in a dictionary
    column_values = df[column_name].tolist()
    column_dict = {column_name: column_values}

    # Create a new DataFrame from the dictionary
    df_new = pd.DataFrame(column_dict)

    # Split the column into three temporary columns
    df_new[['Rebounds (OR)', 'Rebounds (DR)', 'Rebounds (TOT)']] = df_new[column_name].str.split(expand=True)

    # Drop the original 'Rebounds' column
    df_new = df_new.drop(column_name, axis=1)

    # Drop rows with NaN values
    df_new = df_new.dropna()

    # Reset the index of the DataFrame
    df_new = df_new.reset_index(drop=True)

    return df_new



def extract_columns(csv_file_path, column_names):
    # Read the CSV file, skipping the first row and setting the second row as the header
    df = pd.read_csv(csv_file_path, skiprows=1, header=0)

    # Create a new DataFrame containing only the desired columns
    extracted_df = df[column_names]

    return extracted_df

def delete_row_with_dnp_in_folder(CSV_FOLDER):
    files = os.listdir(CSV_FOLDER)

    for file_name in files:
        csv_file_path = os.path.join(CSV_FOLDER, file_name)
        delete_row_with_dnp(csv_file_path)

def delete_row_with_dnp(csv_file_path):
    df = pd.read_csv(csv_file_path)
    df = df[~df.applymap(lambda x: x == 'DNP' or x == '----').any(axis=1)]
    df.to_csv(csv_file_path, index=False)



def process_files_home(CSV_FOLDER):
    files = os.listdir(CSV_FOLDER)

    #print(files)

    

    target_file_name = 'boxscorehome.csv'  # Name of the file to be accessed

    second_file_path = None
    for file_name in files:
        if file_name == target_file_name:
            second_file_path = os.path.join(CSV_FOLDER, file_name)
            break

    if second_file_path is None:
        print(f"File '{target_file_name}' not found.")
        return

    sheet = pd.read_csv(second_file_path)

    # Rest of the code remains unchanged
    row_name = 'Team/Coach'
    new_sheet = sheet.drop(sheet[sheet.iloc[:, 0] == row_name].index)

    output_folder = f"{CSV_FOLDER}/boxscore-home"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file_path = os.path.join(output_folder, 'output.csv')
    new_sheet.to_csv(output_file_path, index=False)


def process_files_away(CSV_FOLDER):
    files = os.listdir(CSV_FOLDER)
    #print(files)

    target_file_name = 'boxscoreaway.csv'  # Name of the file to be accessed

    second_file_path = None
    for file_name in files:
        if file_name == target_file_name:
            second_file_path = os.path.join(CSV_FOLDER, file_name)
            break

    if second_file_path is None:
        print(f"File '{target_file_name}' not found.")
        return

    sheet = pd.read_csv(second_file_path)

    #Rest of the code remains unchanged
    row_name = 'Team/Coach'
    new_sheet = sheet.drop(sheet[sheet.iloc[:, 0] == row_name].index)

    output_folder = f"{CSV_FOLDER}/boxscore-away"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file_path = os.path.join(output_folder, 'output.csv')
    new_sheet.to_csv(output_file_path, index=False)


def process_second_file(CSV_FOLDER):
    boxscore_home_folder = os.path.join(CSV_FOLDER, "boxscore-home")
    files = os.listdir(boxscore_home_folder)

    if len(files) >= 1:
         # Assuming there is only one file inside the 'boxscore-home' folder
        file_name = files[0]
        file_path = os.path.join(boxscore_home_folder, file_name)

        print(file_path)


        
        
    
        #Call your defined functions here
        result = two_pointer(file_path, '2 Points')
        result2 = three_pointer(file_path, '3 Points')
        result3 = field_goals(file_path, 'Field Goals')
        result4 = fouls(file_path, 'Fouls')
        result5 = free_throws(file_path, 'Free Throws')
        result6 = reb(file_path, 'Rebounds')
        column_namex = ['No', 'Min', 'AS', 'TO', 'ST', 'BS', '+/-', 'PTS']
        result7 = extract_columns(file_path, column_namex)

        df = pd.DataFrame(result)
        df2 = pd.DataFrame(result2)
        df3 = pd.DataFrame(result3)
        df4 = pd.DataFrame(result4)
        df5 = pd.DataFrame(result5)
        df6 = pd.DataFrame(result6)
        df7 = pd.DataFrame(result7)

        combined_df = pd.concat([df, df2, df3, df4, df5, df6, df7], ignore_index=True, axis=1)

        # Define your own column names
        column_names = ['two points percentage', 'two points made', 'two points attempts', 'three points percentage', 'three points made', 'three points attempts', 'FG percentage', 'FG made', 'FG attempts', 'Fouls PF', 'Fouls FD', 'Free Throws percentage', 'Free Throws made' ,'free Throws attempts', 'Rebounds OR', 'Rebounds DR', 'Rebounds TOT', 'Player', 'Min', 'AS', 'TO', 'ST', 'BS', 'plus or minus', 'PTS']
        # Assign the column names to the DataFrame 
        combined_df.columns = column_names
        new_combined_df = combined_df.drop(0)

        output_folder = f"{CSV_FOLDER}"
        output_file_path = os.path.join(output_folder, 'final-home.csv')

        new_combined_df.to_csv(output_file_path, index=False)

def process_third_file(CSV_FOLDER):
    boxscore_away_folder = os.path.join(CSV_FOLDER, "boxscore-away")
    files = os.listdir(boxscore_away_folder)

    if len(files) >= 1:
         # Assuming there is only one file inside the 'boxscore-home' folder
        file_name = files[0]
        file_path = os.path.join(boxscore_away_folder, file_name)

        print(file_path)
   
       

        # Call your defined functions here
        result = two_pointer(file_path, '2 Points')
        result2 = three_pointer(file_path, '3 Points')
        result3 = field_goals(file_path, 'Field Goals')
        result4 = fouls(file_path, 'Fouls')
        result5 = free_throws(file_path, 'Free Throws')
        result6 = reb(file_path, 'Rebounds')
        column_namex = ['No', 'Min', 'AS', 'TO', 'ST', 'BS', '+/-', 'PTS']
        result7 = extract_columns(file_path, column_namex)

        df = pd.DataFrame(result)
        df2 = pd.DataFrame(result2)
        df3 = pd.DataFrame(result3)
        df4 = pd.DataFrame(result4)
        df5 = pd.DataFrame(result5)
        df6 = pd.DataFrame(result6)
        df7 = pd.DataFrame(result7)

        combined_df = pd.concat([df, df2, df3, df4, df5, df6, df7], ignore_index=True, axis=1)

        # Define your own column names
        column_names = ['two points percentage', 'two points made', 'two points attempts', 'three points percentage', 'three points made', 'three points attempts', 'FG percentage', 'FG made', 'FG attempts', 'Fouls PF', 'Fouls FD', 'Free Throws percentage', 'Free Throws made' ,'free Throws attempts', 'Rebounds OR', 'Rebounds DR', 'Rebounds TOT', 'Player', 'Min', 'AS', 'TO', 'ST', 'BS', 'plus or minus', 'PTS']
        # Assign the column names to the DataFrame 
        combined_df.columns = column_names
        new_combined_df = combined_df.drop(0)
         
        output_folder = f"{CSV_FOLDER}"
        output_file_path = os.path.join(output_folder, 'final-away.csv')

        new_combined_df.to_csv(output_file_path, index=False)
               