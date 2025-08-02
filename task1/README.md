# Student Result Management API

## Overview

This project is a FastAPI-based API to manage student scores and compute grades. It allows you to create new students, retrieve students by name, and retrieve all students. The student data is persisted to a JSON file named students.json.

## Features

- Create new students with name and subject scores
- Retrieve students by name
- Retrieve all students
- Calculate average score and grade for each student
- Persist student data to students.json file

## Endpoints

- POST /students/: Create a new student with name and subject scores
- GET /students/{name}: Retrieve a student by name
- GET /students/: Retrieve all students

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (for running the API)

## Usage

1. Install the required packages: pip install fastapi uvicorn
2. Run the API: uvicorn main:app 

## API Documentation

The API documentation is available at http://localhost:8000/docs. You can use the documentation to test the API endpoints.

