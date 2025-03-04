For security purpose, we are using env variables for individual's database connection.
Follow the step below to set environment variables.
## On Windows (PowerShell):
```powershell```
- $env:DB_USER="your db username goes here (ex: root)"
- $env:DB_PASSWORD="your password goes here"

## On Mac/Linux:
```Mac/Linux```
- export DB_USER="your db username goes here (ex: root)"
- export DB_PASSWORD="your password goes here"

### To set up db for this project, follow the steps below:
- 1, Run create_tables.py 
- 2, Run import_data.py

# ------------- Below is for log -------------
## March 3, 2025

### Created project
- Implemented basic project setup for db_connection, create_table, and import CSV file
- Fixed db connector to environment variable for safe purpose

# March 4, 2025

### Created md
- Created README.md
- expand branches into main, staging, dev for implementation