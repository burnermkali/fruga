# boxscore-backend

NUKTA SCORESHEET README

This readme provides documentation for nukta score sheet flask app.

OVERVIEW AND PURPOSE

The main purpose of this application is simplify data extraction from the scoresheets which will be uploaded by coaches or team managers.

The table to be extracted is from  a FIBA Boxscore scoresheet in pdf format.

The app extracts 4 tables namely, '5mininterval', 'boxscorehome', 'boxscoreaway', and alalytics. From the pdf i have named tables starting from the top.

The extracted tables are first converted to a csv file then saved in a postgresql database.

INSTALLATION AND SETUP

Create a virtual envirionment

Install dependancies in the requirements.txt file.

NOTE: The library tabula-py required to extract tables will need (java dvelopment kit) jdk-17 to be installed in your machine and PATH set 


DIRECTORY STRUCTURE

The code is stored in a folder called boxscore-backend.

Inside the folder we have

*boxscore-away - This is the folder where the second table from the pdf file is stored in CSV format.

*boxscore-home - This is the folder where the first table from the pdf file is stored in CSV format.

*boxscore - This is the python package that contains all the code files.

*csvs - When the tables are extracted from thhe pdf in raw format, they are first saved in this folder.

*files - The uploaded pdf is saved in this folder


The final edited csvs that are added to the database are saved as:

output-home.csv - The first table from the pdf file.

output-away.csv - The second table from the pdf file.


CONFIGURATION - INSTALLING JAVA DEVELOPMENT KIT

1. Go to official oracle website https://www.oracle.com/ke/java/technologies/downloads/

2. Download jdk17

3. run the installation

4. set path for the jdk

echo 'export PATH="/usr/lib/jvm/jdk-17/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

5. verify the installaton by running java -version

*This is very important, the application will not run untill this requirement is met.



APPLICATION STRUCTURE

The code for the application is found in the folder called boxscore.

Inside the boxscore folder we have:

Folder: static - with the css files

Folder: templates - with the html files

1 __init__.py - This is the starting point for this application. we define the function to create app.

2 main.py - This file contains the flask routes that are used in this application. there is only one route since its one page.

3 functions.py - This file contains all the functions that will do the operations on the various section of the file. 

4. database.py - This file has the database functions to submit different tables into their respective tables

5. db_config.py - Has the credentials required to access the production database.

6. s3.py - Contains the function to upload the pdf file to s3 (Not Active At The Moment)
 
 










