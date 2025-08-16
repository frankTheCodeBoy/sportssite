## 🏟️ SportsSite — Django Sports Portal

[![Django](https://img.shields.io/badge/Django-4.x-green?logo=django)](https://www.djangoproject.com/)  
[![HTML](https://img.shields.io/badge/HTML-44%25-orange?logo=html5)](https://developer.mozilla.org/en-US/docs/Web/HTML)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A dynamic sports web application built with Django. Includes modular apps, media file support, and a custom data ingestion script. Designed for scalability and real-time content updates.

---

### 🧩 Features

- 📰 Sports content management via `sportsApp` and `sportsWeb`  
- 📦 Static and media file handling  
- 📄 Template-driven UI with responsive layout  
- ⚙️ Custom data ingestion via `get_data.py`  
- 🗃️ SQLite database integration  
- 🧱 Modular structure for easy expansion

---

### 📁 Project Structure

```plaintext
sportssite/
├── data/
├── env/
├── media/
├── sportsApp/
├── sportsWeb/
├── staticfiles/
├── templates/
├── db.sqlite3
├── get_data.py
├── manage.py
├── .gitignore
└── README.md
```

---

### 🚀 Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/frankTheCodeBoy/sportssite.git
   cd sportssite
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv env
   source env/bin/activate  # or env\Scripts\activate on Windows
   pip install django
   ```

3. Run migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

---

### 🎯 Purpose

This project was built to:
- Explore Django app modularity  
- Practice media and static file integration  
- Implement custom data ingestion workflows  
- Serve as a scalable base for sports-related content platforms

---

### 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

