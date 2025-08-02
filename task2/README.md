# Mini Shopping API with Cart

## Overview

This project is a simple shopping API that allows users to browse products, add products to their cart, and checkout. The API is built using FastAPI and uses a JSON file to store cart data.

## Features

- Browse products
- Add products to cart
- Checkout cart
- Save cart data to JSON file

## Endpoints

- GET /products/: Get a list of all products
- POST /cart/add: Add a product to the cart
- GET /cart/checkout: Checkout the cart and get the total cost

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (for running the API)
- JSON (for storing cart data)

## Usage

1. Install the required packages: pip install fastapi uvicorn
2. Run the API: uvicorn main:app --reload

## API Documentation

The API documentation is available at http://localhost:8000/docs. You can use the documentation to test the API endpoints.

## Cart Data Storage

The cart data is not stored in a database, but rather in a JSON file named cart.json. This file is created automatically when a product is added to the cart.
