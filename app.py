from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
users = {}

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Get a specific user by ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({user_id: user})
    return jsonify({'error': 'User not found'}), 404

# Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    user_id = str(data.get('id'))
    if user_id in users:
        return jsonify({'error': 'User already exists'}), 400
    users[user_id] = data
    return jsonify({'message': 'User added successfully'}), 201

# Update an existing user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    users[user_id].update(request.json)
    return jsonify({'message': 'User updated successfully'})

# Delete a user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
