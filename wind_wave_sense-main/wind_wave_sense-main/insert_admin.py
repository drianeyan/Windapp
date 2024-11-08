from werkzeug.security import generate_password_hash
import mysql.connector

# Connect to your database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123',
    database='wind_wave_direction'
)
cursor = connection.cursor()

# Define the new admin details
admin_username = 'admin'  # Replace with the actual admin username
admin_email = 'admin@example.com'    # Replace with the actual admin email
admin_password = 'password'  # Replace with the actual password

# Hash the password
hashed_password = generate_password_hash(admin_password)

# Insert the new admin into the database
cursor.execute('''INSERT INTO admin (username, email, password)
                  VALUES (%s, %s, %s)''', (admin_username, admin_email, hashed_password))
connection.commit()

print("Admin inserted successfully!")
cursor.close()
connection.close()
