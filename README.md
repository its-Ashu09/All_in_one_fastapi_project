🚀 Blog API (FastAPI + JWT + PostgreSQL)

A backend project built using FastAPI that provides a complete Blog Management System with User Authentication (JWT).
This project demonstrates how to build secure and scalable REST APIs with modern backend technologies.

📌 Overview

This project allows users to:

Register and login securely
Create, read, update, and delete blogs
Access only their own data using authentication

It follows best practices like modular structure, dependency injection, and token-based security

✨ Features
🔐 User Authentication (JWT)
Secure login system
Token-based authorization
👤 User Management
Register new users
Store hashed passwords
📝 Blog CRUD Operations
Create blog
Get all blogs
Update blog
Delete blog
🔒 Protected Routes
Only authenticated users can access certain APIs
🔗 Database Relationships
One user → multiple blogs

🛠️ Tech Stack
FastAPI – Backend framework
SQLAlchemy – ORM
PostgreSQL – Database
JWT (python-jose) – Authentication
Passlib (bcrypt) – Password hashing
Uvicorn – ASGI server

⚙️ Installation
git clone <https://github.com/its-Ashu09/All_in_one_fastapi_project.git)>
pip install -r requirements.txt

🚀 Run the Application
uvicorn main:app --reload

🔑 Authentication Flow
User logs in via /login
Receives JWT access token
Sends token in header.

🔗 Database Design
👤 User Table
id
name
email
password
📝 Blog Table
id
title
body
user_id (Foreign Key)

👉 Relationship:
One User → Many Blogs

🎯 Learning Outcomes
Build REST APIs with FastAPI
Implement JWT authentication
Use SQLAlchemy ORM
Handle relationships in databases
Deploy backend applications
