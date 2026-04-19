# Mini CERN Document API

A simple RESTful API for document management, inspired by repository-style platforms such as CERN CDS.

## Purpose
This project was developed to strengthen my Python backend skills using Flask, PostgreSQL, SQLAlchemy, and Docker.

## Features
- REST API built with Flask
- CRUD operations for document records
- PostgreSQL integration
- SQLAlchemy ORM usage
- Dockerized local database setup

## Tech Stack
- Python
- Flask
- PostgreSQL
- SQLAlchemy
- Docker

## API Endpoints
- `GET /health`
- `GET /documents`
- `GET /documents/<id>`
- `POST /documents`
- `PUT /documents/<id>`
- `DELETE /documents/<id>`

## Example Request Body
```json
{
  "title": "CERN Note 001",
  "author": "Murat Tuzlali",
  "description": "First test document"
}

## Notes
On Windows environments, PostgreSQL was exposed on port 5433 to avoid conflicts with an existing local PostgreSQL service running on the default port (5432).