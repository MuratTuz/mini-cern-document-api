# Mini CERN Document API

A simple RESTful API for document management, inspired by document repository platforms such as CERN CDS.

## Purpose
This project was developed to strengthen my Python backend skills using Flask, PostgreSQL, SQLAlchemy, and Docker.

## Features
- Flask-based REST API
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

### Health Check
- `GET /health`

### Documents
- `GET /documents`
- `GET /documents/<id>`
- `POST /documents`
- `PUT /documents/<id>`
- `DELETE /documents/<id>`

## Example Document Payload
```json
{
  "title": "CERN Note 001",
  "author": "Murat Tuzlali",
  "description": "First test document"
}