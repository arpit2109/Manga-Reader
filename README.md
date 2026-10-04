# Manga Reader

## Existing GitHub documentation

<!-- PROJECT LOGO -->
<div align="center">
  
# 📖 Manga Reader  
✨ *A Safe & Ad-Free Web Manga Reader Platform* ✨  

A secure and user-focused web platform designed to provide fans with an **uninterrupted, ad-free reading experience**.  

---

</div>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/patelarpit21/manga-reader?style=for-the-badge&color=blueviolet">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/patelarpit21/manga-reader?style=for-the-badge&color=blue">
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/patelarpit21/manga-reader?style=for-the-badge&color=green">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge">
</p>

---

## ✨ Overview  
Welcome to the **Manga Reader Project**!  
This project was created to solve a common frustration: unsafe and ad-filled manga sites.  
Our goal was to design a **clean, lightweight, and enjoyable reading environment** for manga enthusiasts.  

It’s a **front-end only** solution, optimized for speed, accessibility, and seamless user experience.

---

## 📋 Table of Contents
- 🌟 [Features](#-features)  
- 🛠️ [Technology Stack](#️-technology-stack)  
- 🚀 [Getting Started](#-getting-started)  
- 📂 [Project Structure](#-project-structure)  
- 🔮 [Future Scope](#-future-scope)  
- 📄 [License](#-license)  

---

## 🌟 Features
✅ **Seamless Reading:** Smooth browsing & immersive manga viewer.  
✅ **Responsive Design:** Perfectly adapts on desktop, tablet, and mobile.  
✅ **Optimized Performance:** Compressed images = faster loading.  
✅ **Simple Navigation:** Effortless chapter & series switching.  

---

## 🛠️ Technology Stack

- **HTML5:** Semantic tags (`<header>, <nav>, <main>, <section>, <footer>`) for accessibility & SEO.  
- **CSS3:** Custom styling in `CSS/style.css` and `CSS/style1.css` for unique layout & design.  
- **Responsive Design:** Mobile-first approach with Media Queries.  
- **Flexbox & Grid:** Modern CSS layouts for galleries and components.  
- **Bootstrap:** Utilized grid system and pre-styled UI components (navbars, cards, buttons).  
- **JavaScript:** Client-side interactivity, basic DOM manipulation for navigation/events.  

---

## 🚀 Getting Started

This is a **front-end only project** (no backend). Setup is incredibly simple.  

### ✅ Prerequisites
- A modern browser (Chrome, Firefox, Edge, etc.)  
- Optional: Code editor (VS Code recommended)  

### ⚡ Installation
```bash
# Clone the repository
git clone https://github.com/patelarpit21/manga-reader.git

# Navigate into project folder
cd manga-reader
```

## 📂 Project Structure
```bash
manga-reader/
│
├── CSS/  
│   ├── style.css        # Main styles (layout, components)  
│   └── style1.css       # Additional section-specific styles  
│
├── IMAGE/  
│   ├── manga-covers/    # Manga cover images  
│   └── backgrounds/     # Backgrounds & GIFs  
│
├── chapter-1/           # Example chapter images  
│   └── page-*.jpg  
│
├── ALL.html             # Manga listings page  
├── ALL1.html            # Alternative listing page  
├── comic.html           # Individual manga details  
├── magareader.html      # Homepage (main entry point)  
└── reader.html          # Chapter viewer page
```
## 🔮 Future Scope
📌 User Login & Bookmarks → Save reading progress.  
📌 Backend Integration → Add DB like SQLite/PostgreSQL for content & users.  
📌 Dark Mode & Themes → Personalize the experience.  
📌 Advanced Search → Filter by genre, author, or status.  

## 📄 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute this project.

<div align="center">
  <br><br>
💡 Built with passion for manga enthusiasts.
No ads. No distractions. Just stories. 🎉

</div> 

## Local application documentation

﻿# Manga Reader

A manga reading application with a React frontend and Django backend/API.

## Technologies

React 19, Create React App, JavaScript, Python, and Django.

## Setup and run

Start the backend:

```bash
cd backend
python -m venv .venv
.venv/Scripts/activate
python -m pip install django
python manage.py migrate
python manage.py runserver
```

Start the frontend in another terminal:

```bash
cd frontend
npm install
npm start
```

The backend currently has no requirements file; install any additional dependencies required by the API as needed.

