from flask import Flask, jsonify, request
import mysql.connector
app = Flask(__name__)
# Configure the database connection
import pyodbc

# Connect to the database
try:
    connection = pyodbc.connect("Driver={SQL Server};Server=Angel\MSSQLSERVER04;Database=data;")
    cursor = connection.cursor()
    print("Connected to MySQL database")
except pyodbc.Error as err:
    print(f"Failed to connect to MySQL database: {err}")

@app.route('/get-data')
def getdata():
    connection = pyodbc.connect("Driver={SQL Server};Server=Angel\\MSSQLSERVER04;Database=data;")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM records")
    columns = [column[0] for column in cursor.description]
    data = [dict(zip(columns, row)) for row in cursor.fetchall()]
    connection.close()
    return jsonify({'data': data})

@app.route('/get-user/<int:id>')
def getuniquedata(id):
    connection = pyodbc.connect("Driver={SQL Server};Server=Angel\\MSSQLSERVER04;Database=data;")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM records WHERE id=?", (id,))
    print("SELECT * FROM records WHERE id=?", (id,))
    columns = [column[0] for column in cursor.description]
    data = [dict(zip(columns, row)) for row in cursor.fetchall()]
    connection.close()
    return jsonify({'data': data})



@app.route('/delete-data/<int:id>', methods=['DELETE'])
def delete_data(id):
    connection = pyodbc.connect("Driver={SQL Server};Server=Angel\\MSSQLSERVER04;Database=data;")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM records WHERE id=?", (id,))
    connection.commit()
    connection.close()
    return jsonify({'message': 'Record deleted successfully'})

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Ensure all required fields are present in the request
    required_fields = ['id', 'first_name', 'last_name', 'company_name', 'city', 'state', 'zip', 'email', 'web', 'age']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    connection = pyodbc.connect("Driver={SQL Server};Server=Angel\\MSSQLSERVER04;Database=data;")
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO records (id, first_name, last_name, company_name, city, state, zip, email, web, age) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (data['id'], data['first_name'], data['last_name'], data['company_name'], data['city'], data['state'], data['zip'], data['email'], data['web'], data['age']))
    connection.commit()
    connection.close()
    return jsonify({'message': 'User created successfully'}), 201




@app.route('/api/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    connection = pyodbc.connect("Driver={SQL Server};Server=Angel\\MSSQLSERVER04;Database=data;")
    cursor = connection.cursor()

    # Check if user exists
    cursor.execute("SELECT * FROM records WHERE id=?", (id,))
    user = cursor.fetchone()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Update user details
    update_fields = ['first_name', 'last_name', 'age']
    for field in update_fields:
        if field in data:
            cursor.execute(f"UPDATE records SET {field}=? WHERE id=?", (data[field], id))

    connection.commit()
    connection.close()
    return jsonify({'message': 'User details updated successfully'}), 200
if __name__ == '__main__':
    app.run(debug=True)