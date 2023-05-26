import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Execute a query to retrieve all data from a specific table
cursor.execute('SELECT * FROM power_app_asistencia')
data = cursor.fetchall()

# Retrieve column names from the cursor description
columns = [desc[0] for desc in cursor.description]

# Define the output CSV file path
csv_file = r'C:\Users\Usuario\Downloads\output2.csv'

# Write the data to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the column names to the CSV file
    writer.writerow(columns)
    
    # Write the data rows to the CSV file
    writer.writerows(data)

# Close the database connection
conn.close()

print('Data has been exported to', csv_file)
