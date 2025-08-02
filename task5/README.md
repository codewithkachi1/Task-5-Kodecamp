# Simple Contact API

## Overview

This project is a simple FastAPI contact management system. It allows users to create contacts, retrieve contacts, and update contacts.

## Features

- Create new contacts
- Retrieve contacts (with optional filtering by name)
- Update contacts
- Use path and query parameters
- Store data in a dictionary
- Handle invalid input gracefully

## Endpoints

- POST /contacts/: Create a new contact
- GET /contacts/: Retrieve contacts (with optional name query parameter)
- POST /contacts/{name}: Update a contact by name

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (for running the API)

API Documentation

The API documentation is available at http://localhost:8000/docs. You can use the documentation to test the API endpoints.
