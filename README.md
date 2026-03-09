# 🎓 Django Student Management System

A **web-based Student Management System** built using **Django** that allows administrators to manage student records efficiently.
The system includes **user authentication** and **CRUD operations** for managing student data.

---

## 🚀 Features

* 🔐 User Authentication (Login / Logout)
* ➕ Add New Students
* 📋 View Student List
* ✏️ Update Student Details
* ❌ Delete Student Records
* 🗄️ MySQL Database Integration
* 🧩 Function-Based Views in Django
* 🖥️ Simple and Clean UI

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Database:** MySQL
* **Frontend:** HTML, CSS, Bootstrap
* **Version Control:** Git & GitHub

---

<!-- ## 📁 Project Structure

django-student-management-system
│
├── Student_Management_System
│   ├── manage.py
│   ├── Student_Management_System
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── student_app
│       ├── models.py
│       ├── views.py
│       ├── forms.py
│       └── templates
│
├── requirements.txt
├── .gitignore
└── README.md -->

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1️⃣ Clone the Repository
```
git clone https://github.com/omkarpawar2002/django-student-management-system.git
```

### 2️⃣ Navigate to the Project Folder
```
cd django-student-management-system
```

### 3️⃣ Create Virtual Environment
```
python -m venv venv
```

### 4️⃣ Activate Virtual Environment
## Windows:
```
venv\Scripts\activate
```

## Mac/Linux:
```
source venv/bin/activate
```

### 5️⃣ Install Dependencies
```
pip install -r requirements.txt
```

<!-- ### 6️⃣ Configure MySQL Database

Update the database settings in:

Student_Management_System/settings.py

Example:

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'student_db',
'USER': 'root',
'PASSWORD': 'your_password',
'HOST': 'localhost',
'PORT': '3306',
}
} -->

### 7️⃣ Apply Migrations
```
python manage.py makemigrations
```

```
python manage.py migrate
```

### 8️⃣ Run the Development Server
```
python manage.py runserver
```

## Now open your browser and go to:
```
http://127.0.0.1:8000/
```

---

## 📸 Screenshots

You can add screenshots of the project interface here.

Example:

screenshots/
├── login_page.png
├── dashboard.png
└── student_list.png

---

## 🔮 Future Improvements

* Role-based authentication
* Student search functionality
* Pagination
* REST API integration
* Deployment on cloud platform

---

## 👨‍💻 Author

**Omkar Pawar**

GitHub:
https://github.com/omkarpawar2002

---

## ⭐ Support

If you like this project, consider giving it a **star ⭐ on GitHub**.
