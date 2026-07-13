# 🐝 Honeybee Business Listings Dashboard

## 📌 Project Overview

This project is a Business Listings Dashboard developed as part of the Honeybee Digital Python Internship Assignment.

The application stores business listings in a MySQL database, provides FastAPI APIs, and displays dashboard reports using a React frontend.

---

## 🚀 Tech Stack

### Frontend
- React.js
- Recharts

### Backend
- FastAPI
- SQLAlchemy

### Database
- MySQL

### Language
- Python

---

## 📊 Features

- Add New Business Listing
- View All Listings
- Search by City
- Search by Category
- Update Listing
- Delete Listing
- Bulk Insert 500 Business Listings
- Dashboard Cards
- City Wise Business Count
- Category Wise Business Count
- Source Wise Business Count
- Bar Chart
- Pie Chart

---

## 📁 Project Structure

```
Honeybee_Assignment/
│
├── backend/
│   ├── main.py
│   ├── crud.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── generate_data.py
│
├── frontend/
│   ├── src/
│   ├── package.json
│
└── README.md
```

---

## ⚙️ Backend Setup

```bash
cd backend

pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install pymysql
pip install faker

uvicorn main:app --reload
```

---

## ⚙️ Frontend Setup

```bash
cd frontend

npm install

npm install recharts

npm run dev
```

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /listings | Get All Listings |
| POST | /listings | Add Listing |
| PUT | /listings/{id} | Update Listing |
| DELETE | /listings/{id} | Delete Listing |
| POST | /bulk-insert | Bulk Insert Data |
| GET | /dashboard/city | City Report |
| GET | /dashboard/category | Category Report |
| GET | /dashboard/source | Source Report |

---

## 📊 Database

Table Name:

listing_master

Fields:

- id
- business_name
- category
- city
- address
- phone
- source
- created_at

---

## 📌 Sample Data

Due to scraping restrictions and website policies, realistic sample business listings were generated using Python Faker.

The generated data was imported into MySQL using the Bulk Insert API.

---

## 🚀 Future Improvements

- User Authentication
- Export Reports
- Pagination
- Advanced Filters
- Live Dashboard

---

## 👨‍💻 Developed By

Siddharth Bharadwaj