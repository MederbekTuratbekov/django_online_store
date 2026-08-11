# Product Catalog Management System

> Django-powered product catalog backend with full CRUD via Class-Based Views.
> Non-technical teams can manage inventory through a clean web UI — no database access needed.

[![Python](https://img.shields.io/badge/Python-3.11-blue)]()
[![Django](https://img.shields.io/badge/Django-5.x-green)]()
[![SQLite](https://img.shields.io/badge/DB-SQLite-lightgrey)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

---

## Problem

E-commerce teams waste hours managing product data through raw DB access or spreadsheets —
leading to inconsistent listings, pricing errors, and slow time-to-market.

---

## Solution

Full product lifecycle management: create → update → deactivate.
Form-driven UI with image support, category filtering, and type classification.

---

## Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/` | List all products |
| GET | `/<pk>/` | Product detail + image |
| GET/POST | `/create/` | Create product |
| GET/POST | `/<pk>/update/` | Update product |
| GET/POST | `/<pk>/delete/` | Delete product |

---

## Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.11 |
| Framework | Django 5.x |
| Database | SQLite (dev) / PostgreSQL-ready |
| Forms | Django ModelForm |
| Media | Pillow |
| Config | python-dotenv |
| Views | Class-Based Views |

---

## How to Run

```bash
git clone https://github.com/your-username/product-catalog
cd product-catalog
pip install django pillow python-dotenv
```

```bash
echo "SECRET_KEY='your-secret-key'" > .env
python manage.py migrate
python manage.py runserver
```

Open: `http://localhost:8000/`

---

## Project Structure
```django_online_store/
    .gitignore
    readme.md
    online_store/
    ├── db.sqlite3
    ├── manage.py
    ├── requirements.txt
    ├── media/
    ├── online_store/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── store_app/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── forms.py
        ├── migrations/
        ├── models.py
        ├── templates/
        │   ├── product_list.html
        │   ├── product_detail.html
        │   ├── product_create.html
        │   ├── product_update.html
        │   └── product_delete.html
        ├── tests.py
        ├── urls.py
        └── views.py
```
---

## Key Decisions

- **5 CBVs** — ListView, DetailView, CreateView, UpdateView, DeleteView — zero boilerplate
- **ModelForm** — only 7 editable fields exposed; `created_date` hidden from users
- **CASCADE delete** — deleting a category removes its products; no orphan records
- **Media files** — Pillow + `MEDIA_URL` routing; images load in all views out of the box
- **python-dotenv** — `SECRET_KEY` loaded from `.env`; no hardcoded secrets

---
