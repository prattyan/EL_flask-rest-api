# 🧑‍💻 User Management REST API with Flask

This is a basic RESTful API built with **Flask** that allows you to manage user data using standard HTTP methods.

---

## 📌 Features

- Create (POST) a new user
- Read (GET) all users or a single user by ID
- Update (PUT) existing user data
- Delete (DELETE) a user

---

## 🛠️ Tech Stack

- Python 3.x
- Flask
- Postman or Curl (for testing)

---

## 📁 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/prattyan/EL_flask-rest-api.git
cd user-api-flask
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install Flask
```

### 4. Run the App

```bash
python app.py
```

App runs at: `http://127.0.0.1:5000/`

---

## 🚀 API Endpoints

| Method | Endpoint        | Description            |
|--------|------------------|------------------------|
| GET    | `/users`         | Get all users          |
| GET    | `/users/<id>`    | Get user by ID         |
| POST   | `/users`         | Add a new user         |
| PUT    | `/users/<id>`    | Update existing user   |
| DELETE | `/users/<id>`    | Delete a user          |

---

## 🧪 Sample JSON for POST/PUT

```json
{
  "id": "1",
  "name": "John Doe",
  "email": "john@example.com"
}
```

---

## 📬 Example CURL Command

```bash
curl -X POST http://127.0.0.1:5000/users \
-H "Content-Type: application/json" \
-d '{"id": "1", "name": "John Doe", "email": "john@example.com"}'
```

---

## ✅ Outcome

You'll learn the **basics of building REST APIs using Flask**, including handling:
- Routes
- JSON data
- CRUD operations

---

## 🧑‍🎓 Author

**Prattyan Ghosh** – Python Developer Intern at Elevate Labs  
