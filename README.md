# 🏨 Hotel Booking System

A backend-based **Hotel Booking Management System** developed using **Python and Django**. The project provides a structured backend for managing hotels, rooms, customers, bookings, payments, amenities, reviews, staff, offers, and invoices through the Django Admin Panel.

---

## 📌 Project Overview

The Hotel Booking System is designed to simplify hotel management and booking operations by maintaining hotel-related information in a centralized database.

The project is developed using Django's **Model-View-Template (MVT)** architecture, with the main focus on backend development and database management.

The system allows administrators to manage hotel records, room information, customers, bookings, payments, amenities, reviews, staff, offers, and invoices using the Django Administration Panel.

---

## 🚀 Features

- 🏨 Hotel Management
- 🛏️ Room Management
- 🏷️ Room Type Management
- 👤 Customer Management
- 📅 Hotel Booking Management
- 💳 Payment Management
- ⭐ Review Management
- 🛜 Amenity Management
- 🔗 Room-Amenity Relationships
- 🎁 Offer Management
- 👨‍💼 Staff Management
- 🧾 Invoice Management
- 🔐 Django Superuser Authentication
- ⚙️ Django Admin Panel
- 🔄 CRUD Operations
- 🔗 Foreign Key Relationships
- 📊 Database Management
- 🕒 Automatic Timestamps
- 🎨 Customized Django Admin Interface

---

## 🗂️ Models

The project contains **12 major models**:

1. **Hotel**
2. **RoomType**
3. **Room**
4. **Customer**
5. **Booking**
6. **Payment**
7. **Review**
8. **Amenity**
9. **RoomAmenity**
10. **Offer**
11. **Staff**
12. **Invoice**

---

## 🔗 Database Relationships

The project uses Django ORM and Foreign Key relationships to connect different models.

Examples:

- A **Hotel** can have multiple Rooms.
- A **Room** belongs to a Hotel.
- A **Room** belongs to a Room Type.
- A **Customer** can make multiple Bookings.
- A **Booking** is associated with a Room.
- A **Booking** is associated with a Customer.
- A **Booking** can have a Payment.
- A **Booking** can have an Invoice.
- A **Room** can have multiple Amenities.
- A **Review** is associated with a Customer and Hotel.

The project uses more than **8 Foreign Key relationships** as required.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Django | Backend Web Framework |
| SQLite | Database |
| Django ORM | Database Operations |
| Django Admin | Backend Administration |
| HTML/CSS | Basic Admin/Template Support |
| Git | Version Control |
| GitHub | Source Code Management |

---

## 📁 Project Structure

```text
HotelBookingProject/
│
├── booking/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── djangoproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/
│
├── .gitignore
├── requirements.txt
├── manage.py
└── README.md
