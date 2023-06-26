from flask import *
from flask_login import login_required, current_user
import tabula
import PyPDF2
import os
from werkzeug.utils import secure_filename
from .functions import *
from . import db
from .models import User, Scoresheet
from .stats import calculate_rankings
from datetime import datetime




main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


    


@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    def simplify_csv(sheet):
        sheet = Scoresheet.query.filter_by(team=current_user.team).first()
        league = sheet.league
        game_string = sheet.game_string

        if sheet.home_team is not None:
            simplified_name = f"{league} {game_string} - {sheet.home_team} vs {current_user.team}"
        else:
            simplified_name = f"{league} {game_string} - {current_user.team} vs {sheet.away_team}"
        return simplified_name
    
    


    csv_folder_path = 'finals'  # Update with the path to your CSV folder
    csv_files = [f for f in os.listdir(csv_folder_path) if f.endswith('.csv') and f.startswith(current_user.team)]

    selected_csv = request.form.get('csv')  # Get the selected CSV file from the form submission

    if selected_csv:
        csv_file_path = os.path.join(csv_folder_path, selected_csv)

        # Read the selected CSV file and extract player stats
        player_stats_df = pd.read_csv(csv_file_path)

        # Convert player stats DataFrame to a list of dictionaries
        player_stats = player_stats_df.to_dict(orient='records')
    else:
        # Initialize player_stats with default values
        player_stats = [{'Player': '', 'Points': 0, 'Rebounds': 0, 'Assists': 0, 'Blocks': 0, 'Three Points': 0, 'Two Points': 0}]

     # Call the simplify_csv function to get the simplified name

     
    return render_template('dashboard.html', csv_files=csv_files, player_stats=player_stats, team=current_user.team, simplify_csv=simplify_csv)



@main.route('/scoresheet')
@login_required
def upload():
    team = current_user.team
    return render_template('scoresheet.html', team=team)
    
  
    

@main.route('/scoresheet', methods=['POST'])
def upload_post():
   team= request.form.get('team')
   game_date = request.form.get('game_date')
   league = request.form.get('league')
   where = request.form.get('where')
   other_team = request.form.get('other_team')
   file = request.files['file']

   date_string = game_date
   game_date = datetime.strptime(date_string, "%Y-%m-%d")
   game_date = datetime.strftime(game_date, "%d%m%Y")
   
   input_date = game_date
   date_obj =  datetime.strptime(input_date, "%d%m%Y")
   game_string = datetime.strftime(date_obj, "%dth %B %Y")

   os.makedirs('finals', exist_ok=True)

   filename = (file.filename).replace(" ", "")



   user = User.query.filter_by(email=current_user.email).first()
   
   sheet = Scoresheet.query.filter_by(team=current_user.team, game_date=game_date).first()

   if sheet:
        flash('Scoresheet already exists')
        return redirect(url_for('main.upload'))
   new_scoresheet = Scoresheet(team=team, game_date=int(game_date), game_string=game_string,league=league, where=where, filename=filename)
   if where == "scoresheetA":
    new_scoresheet.away_team = other_team
   elif where == "scoresheetB":
    new_scoresheet.home_team = other_team
   db.session.add(new_scoresheet)
   db.session.commit()
  
   
    

    # Update the is_active column to True
   
   CSV_FOLDER = f'scoresheets/{team}/{game_date}'
   UPLOAD_FOLDER = f'pdf/{team}/{game_date}'

   os.makedirs(f'{UPLOAD_FOLDER}', exist_ok=True)
   os.makedirs(f'{CSV_FOLDER}', exist_ok=True)
    
   file.save(os.path.join(UPLOAD_FOLDER, secure_filename(file.filename)))

   file_path = rf'{UPLOAD_FOLDER}/{file.filename}'
   pdf_reader = PyPDF2.PdfReader(file_path)

   num_pages = len(pdf_reader.pages)

   for page in range(num_pages):
        tables = tabula.read_pdf(file_path, pages=page+1, multiple_tables=True)
        extracted_tables = []

        for i, table in enumerate(tables):
            # Remove 'Unnamed' from column headers
            table.columns = [col if not col.startswith('Unnamed') else '' for col in table.columns]

            # Determine the filename based on the table index
            if i == 0:
                filename = f'fivemininterval.csv'
            elif i == 1:
                filename = 'boxscorehome.csv'
            elif i == 2:
                filename = 'boxscoreaway.csv'
            elif i == 3:
                filename = 'analytics.csv'
            else:
                filename = f"table_{page + 1}_{i + 1}.csv"

            # Save the table as a CSV file
            csv_file_path = rf"{CSV_FOLDER}/{filename}"
            table.to_csv(csv_file_path, index=False)


            if i+1 == 4:
                delete_row_with_dnp_in_folder(CSV_FOLDER)
                process_files_home(CSV_FOLDER)
                process_files_away(CSV_FOLDER)
               
                
        process_second_file(CSV_FOLDER)
        process_third_file(CSV_FOLDER)
        if request.form.get('where') == 'scoresheetA':
            csv_file = os.path.join(CSV_FOLDER, 'final-home.csv')
            calculate_rankings(csv_file, team_name=current_user.team, game_date=request.form.get('game_date'))


            csv_file1 = os.path.join(f'{current_user.team}{game_date}rankings.csv')
            #map_csv_to_postgres(csv_file1, team_name=current_user.team, game_date=request.form.get('date'))
            return redirect(url_for('main.dashboard'))
        elif request.form.get('where') == 'scoresheetB':
            csv_file = os.path.join(CSV_FOLDER, 'final-away.csv')
            calculate_rankings(csv_file, team_name=current_user.team, game_date=request.form.get('game_date'))
            
            
            csv_file1 = os.path.join(f'{current_user.team}{game_date}rankings.csv')
            #map_csv_to_postgres(csv_file1, team_name=current_user.team, game_date=request.form.get('date'))
            return redirect(url_for('main.dashboard'))
        else:
            return redirect(url_for('main.scoresheet'))



