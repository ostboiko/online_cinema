fast-api-cinema
🎬 FastAPI Cinema

FastAPI Cinema is an API service for an online cinema platform, built with FastAPI and PostgreSQL. It provides full functionality for user management, movie catalog interaction, shopping cart operations, and order processing.

📦 Features

User registration, login, and authentication
Account activation and password recovery via email tokens
Browse and filter movies by name, IMDb rating, price, and release year
Add reactions and comments to movies
Manage shopping cart: add, remove, clear, and checkout items
View order history
🛠️ Tech Stack

FastAPI
SQLAlchemy
PostgreSQL
Docker / Docker Compose
Alembic (for migrations)
JWT (for authentication)
🚀 Getting Started To run the project:

docker-compose up --build 

Once started, the app will be available at:

🔗 http://localhost:8000

Swagger Documentation:

📚 http://localhost:8000/docs

To use all the features you need to register a user with an email confirmation on /register/ endpoint and then use the credentials on /login/