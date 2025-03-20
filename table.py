import mysql.connector
import pandas as pd
import os

# Database connection
mydb = {
    "host": "localhost",
    "user": "root",
    "password": "Divya99403@",
    "database": "test"
}

# List of CSV files and their corresponding categories
csv_files = {
    "guj.csv": "Gujarati",
    "GK.csv": "GK",
    "c++.csv": "C++",
    "eng.csv": "English"
}

try:
    # Establish MySQL connection
    connection = mysql.connector.connect(**mydb)
    cursor = connection.cursor()

    # Create quiz table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz (
            question VARCHAR(255),
            `options` VARCHAR(255),
            answer VARCHAR(255),
            category VARCHAR(255),
            subcategory VARCHAR(255)
        )
    """)

    # Insert data from each CSV file
    for csv_file, category in csv_files.items():
        if os.path.exists(csv_file):
            print(f"Processing {csv_file}...")

            # Read CSV file
            data = pd.read_csv(csv_file, encoding='utf-8')

            # Ensure correct column names
            data.columns = ["question", "options", "answer", "category", "subcategory"]

            # Set the category for this dataset
            data["category"] = category

            # Prepare SQL query
            columns = ", ".join([f"`{col}`" for col in data.columns])  # Enclose column names in backticks
            placeholders = ", ".join(["%s"] * len(data.columns))  # Placeholders for values
            sql_query = f"INSERT INTO quiz ({columns}) VALUES ({placeholders})"

            # Insert each row
            for row in data.itertuples(index=False):
                cursor.execute(sql_query, tuple(row))

            connection.commit()
            print(f"{csv_file} data inserted successfully.")

        else:
            print(f"Warning: {csv_file} not found. Skipping.")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
