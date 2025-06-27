# 🧩 User Management REST API with Flask

This is a simple REST API project built using **Python and Flask** that manages user data in-memory. It supports full CRUD operations — perfect for learning the basics of RESTful API design.

---

## 🚀 Features

- ✅ Get all users  
- 🔍 Get a user by ID  
- ➕ Add a new user  
- 🛠️ Update an existing user  
- ❌ Delete a user  

---

## 🛠️ Tech Stack

- Python 3.x  
- Flask  
- Postman / curl for testing  

---

## 📁 Project Structure

```
user-api/
├── app.py          # Main Flask app
└── README.md       # Project documentation
```

---

## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Sayantang8/REST-API-with-Flask.git
cd REST-API-with-Flask
```

### 2. Install Dependencies

```bash
pip install flask
```

### 3. Run the App

```bash
python app.py
```

📍 Server runs at: `http://127.0.0.1:5000/`

---

## 📬 API Endpoints

### ➕ Create a User

- **POST** `/users`  
- **Body**:

```json
{
  "id": 1,
  "name": "Sayantan"
}
```

---

### 📥 Get All Users

- **GET** `/users`

---

### 🔍 Get a User by ID

- **GET** `/users/<id>`  
- Example: `/users/1`

---

### 🛠️ Update a User

- **PUT** `/users/<id>`  
- **Body**:

```json
{
  "name": "Updated Name"
}
```

---

### ❌ Delete a User

- **DELETE** `/users/<id>`

---

## 🧪 Test with curl

```bash
# Add a user
curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d "{\"id\":1,\"name\":\"Sayantan\"}"

# Get all users
curl http://127.0.0.1:5000/users

# Get user by ID
curl http://127.0.0.1:5000/users/1

# Update user
curl -X PUT http://127.0.0.1:5000/users/1 -H "Content-Type: application/json" -d "{\"name\":\"Updated Name\"}"

# Delete user
curl -X DELETE http://127.0.0.1:5000/users/1
```

---

## 📝 Notes

- This API uses an in-memory list, so data resets every time you restart the server.  
- Designed for educational/demo purposes.

---

## 📄 License

MIT License

---

## 🙋‍♂️ Author

**Sayantan**  
💬 Drop a ⭐ if you found this helpful!
