# 🐝 Honeybee Business Listings Dashboard

A Full Stack Business Listings Dashboard developed as part of the **Honeybee Digital Python Internship Assignment**.

The application uses **React**, **FastAPI**, **SQLAlchemy**, and **MySQL** to manage business listings and display dashboard analytics.

---

# 📌 Project Overview

This project allows users to manage business listings through a web-based dashboard.

The application provides REST APIs using FastAPI, stores data in MySQL, and displays interactive reports and charts using React.

The project demonstrates:

- Full Stack Development
- REST API Development
- CRUD Operations
- Database Management
- Dashboard Analytics
- Search & Filtering
- Git & GitHub Workflow

---

# 🚀 Tech Stack

## Frontend

- React.js
- Vite
- Axios
- Recharts
- HTML
- CSS

## Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

## Database

- MySQL

## Development Tools

- Visual Studio Code
- Git
- GitHub
- MySQL Workbench

---

# ✨ Features

### Business Management

- Add New Business Listing
- View All Business Listings
- Update Business Listing
- Delete Business Listing

### Search & Filter

- Search by City
- Search by Category

### Dashboard

- Total Business Listings
- City Wise Report
- Category Wise Report
- Source Wise Report
- Bar Chart
- Pie Chart

### Database

- Bulk Insert Business Listings
- SQL Backup Included

---

# 📂 Project Structure

```text
Honeybee_Assignment/
│
├── backend/
│   ├── business_listings.csv
│   ├── crud.py
│   ├── database.py
│   ├── generate_data.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── .gitignore
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
│
├── .gitignore
├── honeybee_db.sql
├── start_project.bat
└── README.md
```

> Note: Local folders such as `venv`, `node_modules`, and `__pycache__` are intentionally excluded because they are generated automatically and are not part of the source code.

---

# ⚙️ Backend Setup

```bash
cd backend

venv\Scripts\activate

uvicorn main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# ⚙️ Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /listings | Get All Listings |
| POST | /listings | Add Listing |
| PUT | /listings/{id} | Update Listing |
| DELETE | /listings/{id} | Delete Listing |
| POST | /bulk-insert | Bulk Insert Sample Data |
| GET | /dashboard/city | City Wise Report |
| GET | /dashboard/category | Category Wise Report |
| GET | /dashboard/source | Source Wise Report |

---

# 🗄️ Database

**Database Name**

```
honeybee_db
```

**Table Name**

```
listing_master
```

**Fields**

- id
- business_name
- category
- city
- address
- phone
- source
- created_at

**Current Records**

```
502 Business Listings
```

---

# 📊 Dashboard Modules

- Dashboard Cards
- Business Listing Table
- Search Filters
- City Wise Analytics
- Category Wise Analytics
- Source Wise Analytics
- Bar Chart
- Pie Chart

---

# 📦 SQL Backup

Database backup file included:

```
honeybee_db.sql
```

This file can be imported directly into MySQL Workbench.

---

# 🧪 Testing

Successfully Tested:

- CRUD Operations
- FastAPI APIs
- Swagger Documentation
- React Dashboard
- Database Connectivity
- Search Functionality
- Charts
- Bulk Insert
- GitHub Repository

---

# 🚀 Future Improvements

- User Authentication
- Pagination
- Export Reports (Excel/PDF)
- Advanced Filters
- Dashboard Enhancements

---

# 👨‍💻 Developed By

**Siddharth Bharadwaj**

Honeybee Digital Python Internship Assignment

---

# ⭐ Thank You

Thank you for reviewing this project.

Feedback and suggestions are always welcome.