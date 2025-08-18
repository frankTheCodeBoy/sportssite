## 🏟️ SportsSite — Django Sports Portal

[![Django](https://img.shields.io/badge/Django-4.x-green?logo=django)](https://www.djangoproject.com/)  
[![HTML](https://img.shields.io/badge/HTML-44%25-orange?logo=html5)](https://developer.mozilla.org/en-US/docs/Web/HTML)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)  
[![Live Demo](https://img.shields.io/badge/Live-Demo-blue?logo=python)](https://billydisu.pythonanywhere.com)

**SportsSite** is a dynamic sports web application built with Django. It features modular apps, media file support, user authentication, and custom data ingestion—designed for scalability and real-time content updates.

---

### 🌐 Live Demo

Explore the live site here:  
🔗 [https://billydisu.pythonanywhere.com](https://billydisu.pythonanywhere.com)

---

### 🧩 Features

- 📰 Sports content management via `sportsApp` and `sportsWeb`  
- 📦 Static and media file handling  
- 📄 Template-driven UI with responsive layout  
- ⚙️ Custom data ingestion via `get_data.py`  
- 🗃️ SQLite database integration  
- 🔐 User registration, login, and profile management  
- 🎥 Sports videos and media highlights  
- 🗣️ Commentary support and category-based content filtering  
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

To run the project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/frankTheCodeBoy/sportssite.git
   cd sportssite
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Apply migrations and start the server**
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

### 🛣️ Roadmap

Planned enhancements for future versions:

- 📊 **Analytics Dashboard** — Track user engagement and content performance  
- 🧠 **AI-Powered Match Predictions** — Integrate basic ML models for forecasting outcomes  
- 📱 **Enhanced Mobile Experience** — Refine UI/UX for smaller screens  
- 🌍 **Multi-language Support** — Add Swahili and French localization  
- 🧪 **Unit & Integration Testing** — Strengthen reliability with automated test coverage  
- 🔔 **User Notifications** — Alert users to new content, match updates, or comments  
- 🗂️ **Advanced Search & Filtering** — Improve content discoverability across categories and highlights

---

### 🛠️ Built With

- 🐍 [Python](https://www.python.org/)  
- 🌿 [Django](https://www.djangoproject.com/)  
- 🗃️ [SQLite](https://www.sqlite.org/index.html)  
- 🎨 HTML, CSS, JavaScript  
- 🧰 Bootstrap (for responsive UI)  
- 🖼️ PythonAnywhere (for deployment)

---

### 🤝 Contributing

Pull requests are welcome! If you'd like to contribute:

1. Fork the repository  
2. Create your feature branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m 'Add feature'`)  
4. Push to the branch (`git push origin feature-name`)  
5. Open a pull request

---

### 👤 Author

**Frank Olum** — IBM & Microsoft Certified Full-Stack Developer  
🔗 [GitHub: frankTheCodeBoy](https://github.com/frankTheCodeBoy)  
💻 Passionate about clean code, scalable systems, and building tools that make sports content shine.

---

### 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

