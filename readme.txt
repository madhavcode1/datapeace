Flask API for Managing User Data
This Flask application provides a RESTful API for managing user data stored in a Microsoft SQL Server database.

Setup
Install the required packages using pip:
bash
Copy code
pip install Flask pyodbc
Ensure you have the correct database configuration in your code (app.py) for connecting to your SQL Server instance:
python
Copy code
db_config = {
    'Driver': '{SQL Server}',
    'Server': 'Angel\\MSSQLSERVER04',
    'Database': 'data',
    'UID': 'your_username',
    'PWD': 'your_password',
}
Replace 'your_username' and 'your_password' with your actual SQL Server username and password.
Run the Flask application:
bash
Copy code
python app.py
Endpoints
Get All Users
URL: /get-data
Method: GET
Description: Retrieves all users from the database.
Response: JSON object containing all user records.
Get a Specific User
URL: /get-user/<int:id>
Method: GET
Description: Retrieves a specific user by ID from the database.
Response: JSON object containing the user record.
Delete a User
URL: /delete-data/<int:id>
Method: DELETE
Description: Deletes a user by ID from the database.
Response: JSON object with a message indicating the deletion was successful.
Create a New User
URL: /api/users
Method: POST
Description: Creates a new user in the database.
Request Payload: JSON object containing user data.
Response: JSON object with a message indicating the user was created successfully.
Update User Details
URL: /api/users/<int:id>
Method: PUT
Description: Updates the details of a user by ID in the database.
Request Payload: JSON object containing the fields to update (first_name, last_name, age).
Response: JSON object with a message indicating the user details were updated successfully.
You can add more details to the README.md file as needed, such as information about the database schema, additional endpoints, or how to use the API.