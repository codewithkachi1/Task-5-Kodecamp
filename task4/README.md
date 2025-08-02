# Notes App API

## Overview

This project is a simple API to manage notes. It allows users to create new notes, read existing notes, update notes, and delete notes. The notes are saved as text files on the server.

## Features

- Create new notes
- Read existing notes
- Update notes
- Delete notes
- Notes are saved as text files on the server

## Endpoints

- POST /notes/: Create a new note
- GET /notes/{title}: Read a note by title
- POST /notes/{title}: Update a note by title
- DELETE /notes/{title}: Delete a note by title

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (for running the API)

## Usage

1. Install the required packages: pip install fastapi uvicorn
2. Run the API: uvicorn main:app --reload

## API Documentation

The API documentation is available at http://localhost:8000/docs. You can use the documentation to test the API endpoints.

## Notes Storage

The notes are saved as text files in the notes directory. Each note is saved with a filename that matches the title of the note.

## Error Handling

The API uses try-except blocks to handle errors. If an error occurs during the creation, reading, updating, or deletion of a note, the API will return a 400 Bad Request response with a detailed error message.
