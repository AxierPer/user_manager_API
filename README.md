# 🚀 User Management API

A simple backend API built with Python and Flask for managing user data. This project supports basic CRUD (Create, Read, Update, Delete) operations for user management and is perfect for learning the fundamentals of backend development in Python. Built with dependency management using **Poetry**.

---

## 📚 Features

- 🌐 **RESTful Endpoints**: Easily manage user data with a set of intuitive endpoints.
- 📦 **Flask Framework**: Lightweight and easy to extend for more complex functionalities.
- 🛡️ **Input Validation**: Ensures valid data and handles errors gracefully.
- 💾 **Extensible**: Simple structure for further enhancements, like adding a database or authentication.

---

## 🛠️ Installation & Setup

Follow these steps to set up the project on your local machine:

### Prerequisites

- **Python 3.7+**
- **Poetry** (for dependency management)

### Clone the Repository

```bash
git clone https://github.com/your-username/user-management-api.git
cd user-management-api
```

## Install Dependencies

Use Poetry to install all the necessary packages:

```bash
poetry install
```

## Activate the Virtual Environment

```bash
poetry shell
```

## Run the API

```bash
In Windows :
python main.py
```

```bash
In Linux :
python3 main.py
```

The API will run on http://127.0.0.1:5000. You can now make requests to the available endpoints.

---

# 📋 API Endpoints

## Here's a list of available API endpoints:

- **GET /user**: Retrieve a list of all users.
- **POST /user**: Create a new user. Requires name, email, and age in the request body.
- **GET /user/<id>**: Retrieve a specific user by ID.
- **PUT /user/<id>**: Update a user's information.
- **DELETE /user/<id>**: Delete a user by ID.

---

# 📝 Example Usage

## Create a New User

```bash
curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d '{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 30
}'
```

## Retrieve All Users

```bash
curl http://127.0.0.1:5000/users
```

---

# 🤝 Contributing

## Feel free to fork this project, create a branch, and submit a pull request! Any contributions are welcome.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

---

# 📧 Contact

## Have questions or suggestions? Feel free to reach out!

- **Email**: [axierperlaz2018@gmail.com](mailto:axierperlaz2018@gmail.com)
- **GitHub**: [AxierPer](https://github.com/AxierPer)

---

# ⭐ Acknowledgments

Thanks to the Python and Flask communities for providing great tools and documentation! Special shoutout to anyone who inspired you.

Enjoy building and happy coding! 🎉

---
