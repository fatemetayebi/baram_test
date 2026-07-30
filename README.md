# Django Services & Orders API

A comprehensive Django REST API for managing users, services, and orders with role-based access control.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Testing with Bruno](#testing-with-bruno)

## 🚀 Overview

This project provides a complete backend solution for a service ordering platform where:
- **Users** can register, login, and manage their profile
- **Admins** can manage services and orders
- **Customers** can browse services and place orders

The system includes JWT authentication, role-based permissions, filtering, searching, pagination, and comprehensive order management.

## ✨ Features

### User Management
- User registration with email/username
- JWT authentication (access & refresh tokens)
- Role-based access control (Admin, Staff, Customer, Support)
- Profile management

### Service Management
- CRUD operations (only admins can create/update/delete)
- Service categorization (SEO, Web Design, Development)
- Search by name 
- Filter by type

### Order Management
- Create orders for services
- Order status management (Pending, Confirmed, Rejected)
- Search by service name
- Order statistics and analytics

## 🛠️ Tech Stack

- **Backend**: Django 4.2+, Django REST Framework
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Database**: SQLite (default), PostgreSQL (recommended for production)
- **Filtering**: django-filter
- **API Documentation**: Bruno (API client)

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)

## 🧪 Testing with Bruno

This project includes a Bruno collection file that contains all pre-configured API requests for testing.

### What is Bruno?
[Bruno](https://www.usebruno.com/) is a free, open-source API client that stores collections locally on your machine.

### How to use:

1. **Download and install Bruno** from [usebruno.com](https://www.usebruno.com/download)

2. **Import the collection**:
   - Open Bruno
   - Click `Import Collection`
   - Select the file: `bruno/baram_bruno.json`

3. **Set up environment variables** in Bruno:
