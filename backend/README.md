# 🛡️ PrivacyGuard Backend

PrivacyGuard Backend is a Django REST Framework application that performs automated website privacy and security analysis.

It scans a website and evaluates its security posture by analyzing HTTPS configuration, HTTP security headers, cookies, session management, trackers, and generates an overall security score with actionable recommendations.

---

## 🚀 Features

- 🔒 HTTPS Security Analysis
- 🛡️ HTTP Security Header Analysis
- 🍪 Cookie Security Analysis
- 🔑 Session Security Checks
- 👁️ Tracker Detection
- 📊 Overall Security Score
- 💡 Security Recommendations
- 🌐 REST API

---

## 🛠 Tech Stack

- Python 3
- Django
- Django REST Framework
- Requests
- SQLite (Development)

---

## 📂 Project Structure

```
backend/
│
├── analysis/
│   ├── services/
│   └── ...
│
├── scanner/
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── services/
│
├── reports/
├── config/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/PrivacyGuard.git
```

### Navigate

```bash
cd backend
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

---

## 📡 API Endpoint

### Scan Website

```
POST /api/scan/
```

### Request

```json
{
  "url": "https://github.com"
}
```

### Response

Returns:

- Overall Security Score
- HTTPS Analysis
- Security Headers
- Cookie Analysis
- Session Analysis
- Tracker Detection
- Security Recommendations

---

## 🔮 Future Improvements

- OWASP Top 10 Security Checks
- SSL Certificate Validation
- DNS Security Analysis
- PDF Report Generation
- Scan History
- User Authentication
- PostgreSQL Support

---

## 👩‍💻 Author

**Ananya A M**

Computer Science Engineering Student

---

## 📄 License

This project is intended for educational, portfolio, and learning purposes.
