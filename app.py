from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory store
users = []

# Root route (for browser)
@app.route('/')
def home():
    return "✅ User Management API is running!", 200

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# Get a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({'message': 'User not found'}), 404

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data:
        return jsonify({'message': 'Invalid request'}), 400

    if any(u['id'] == data['id'] for u in users):
        return jsonify({'message': 'User with this ID already exists'}), 400

    users.append({'id': data['id'], 'name': data['name']})
    return jsonify({'message': 'User created successfully'}), 201

# Update user info
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    data = request.get_json()
    if 'name' in data:
        user['name'] = data['name']
    return jsonify({'message': 'User updated successfully'}), 200

# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    if not any(u['id'] == user_id for u in users):
        return jsonify({'message': 'User not found'}), 404

    users = [u for u in users if u['id'] != user_id]
    return jsonify({'message': 'User deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
