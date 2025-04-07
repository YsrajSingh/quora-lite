# 🧠 Quora Clone – Django Assignment

A mini Quora-style Q&A web app built with Django. Users can sign up, post questions, answer others' questions, like answers, and log out.

---

## 🚀 Features

- User Registration & Login
- Post Questions
- View All Questions
- Answer Questions
- Like Answers (one like per user per answer)
- Logout functionality

---

## 💠 Tech Stack

- **Backend**: Django 4.x
- **Database**: PostgreSQL
- **Auth**: Django’s built-in authentication
- **Frontend**: HTML (Django templates)
- **Containerization**: Docker & Docker Compose

---

## 📦 Project Structure

```
quora_clone/
├── app/                  # Django project
│   ├── questions/        # App for questions, answers, likes
│   ├── templates/        # HTML templates
│   └── manage.py
├── Dockerfile
├── docker-compose.yml
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/quora-clone.git
cd quora-clone
```

### 2. Create `.env` File

```env
DEBUG=True
SECRET_KEY=django-insecure-key
POSTGRES_DB=quora_clone
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

### 3. Build & Run with Docker

```bash
docker compose up --build
```

Visit [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🧪 Testing the App

1. Register a new user.
2. Post a question.
3. View all questions.
4. Answer a question.
5. Like an answer.
6. Logout and try logging back in.

---

## 📝 Future Improvements

- Edit/Delete questions and answers
- Pagination & search
- User profiles
- UI enhancements with Bootstrap

---

## 📸 Screenshots

_Add screenshots of key features like posting a question, answering, and liking._

---

## 👨‍💻 Author

- **Yashraj Singh** – [LinkedIn](https://www.linkedin.com/in/your-profile) | [GitHub](https://github.com/yourusername)

---

## 📬 Contact

If you have any questions or suggestions, feel free to reach out at:  
**careers@transportsimple.com**
