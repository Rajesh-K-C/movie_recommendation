# 🎬 Movie Recommendation System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Made with Python](https://img.shields.io/badge/framework-Django-blue)](#)

A full-stack Movie Recommendation System that allows users to discover movies based on popularity, genre, and content-based filtering using machine learning. Built with a Django + TypeScript + Tailwind CSS.

## 📦 Tech Stack

- Python
- Django
- TypeScript
- Tailwind CSS
- PostgreSQL / SQLite (customizable)
- Machine Learning (Cosine Similarity, Pandas, etc.)

---

## ✨ Features

### User Features
- 🔍 Browse and search for movies
- ❤️ Like and view history-based recommendations
- 🎬 Movie detail pages with genre, language, cast, and descriptions

### Admin Features
- 🔧 Add, update, and delete movies, genres, and languages
- 📈 View movie popularity based on user interactions

### Recommendation System
- 📌 Content-based filtering using cosine similarity
- 📊 Popularity-based sorting (recent views & likes)

---

## 🛠️ Installation

## Prerequisites
- Python >=3.12
- Node.js and npm

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Rajesh-K-C/movie_recommendation.git
   cd movie_recommendation
2. Create and activate virtual environment

    You can choose either pip or uv for installing dependencies:
    
    Option 1: Using pip
    ```bash
    # Create virtual environment
    # macOS/Linux:
    python3 -m venv venv
    # Windows:
    py -m venv venv

    # Activate the environment
    # macOS/Linux:
    source .venv/bin/activate
    # Windows:
    venv\Scripts\activate

    # Install dependencies
    pip install -r requirements.txt
    ```

    Option 2: Using uv (Faster alternative)
    ```bash
    # Install uv (if not installed)
    pip install uv

    # Create and activate environment
    uv venv venv
    source venv/bin/activate   # macOS/Linux
    venv/Scripts/activate      # Windows

    # Install using uv
    uv sync
    ```
3. Run migrations and create superuser
    ```bash
    # macOS/Linux:
    python3 manage.py migrate
    python3 manage.py createsuperuser
    # Windows:
    py manage.py migrate
    py manage.py createsuperuser
    ```
4. Start the server
    ```bash
    # macOS/Linux:
    python3 manage.py runserver
    # Windows:
    py manage.py runserver
    ```
5. Install Tailwind CSS
    ```bash
    npm install
    ```
6. Start the Tailwind CLI build process
    ```bash
    npm run watch:css
    ```
7. Install TypeScript(Optional)
    ```bash
    # install TypeScript
    npm install -g typescript
    # compile TypeScript
    tsc --watch
    ```
## 🙌 Contributing
Contributions are welcome! <br/>
Please open an issue or submit a PR with improvements or fixes.
## 📜 License
This project is licensed under the MIT License.
You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

## 📧 Contact
Developed by <a href="https://rajesh-kc.com.np"> Rajesh KC </a> <br/>
For questions, suggestions, or collaborations, feel free to reach out!
