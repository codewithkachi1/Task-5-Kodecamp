# Job Application Tracker API

## Overview

This project is a simple API to manage and search job applications. It allows users to create new job applications, retrieve all job applications, and search job applications by status.

## Features

- Create new job applications
- Retrieve all job applications
- Search job applications by status
- Save and load job applications from a JSON file

## Endpoints

- POST /applications/: Create a new job application
- GET /applications/: Retrieve all job applications
- GET /applications/search: Search job applications by status

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (for running the API)
- JSON (for storing job applications)

## Usage

1. Install the required packages: pip install fastapi uvicorn
2. Run the API: uvicorn main:app --reload

## API Documentation

The API documentation is available at http://localhost:8000/docs. You can use the documentation to test the API endpoints.

## Job Application Data Storage

The job application data is stored in a JSON file named applications.json. This file is created automatically when a new job application is created.

## Error Handling

The API uses try-except blocks to handle input errors. If an error occurs during the creation or search of job applications, the API will return a 400 Bad Request response with a detailed error message.

