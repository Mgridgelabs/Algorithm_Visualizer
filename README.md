# Algorithm_Visualizer

## Overview
The Algorithm Visualizer is a web application built with Flask and Flask-RESTX that provides a visual representation of various sorting algorithms. Users can submit a list of integers, and the application will return the steps taken by the selected sorting algorithm. This project aims to help users understand how different sorting algorithms work through visualization.

## Features
- RESTful API for sorting algorithms
- Support for multiple sorting algorithms (e.g., Bubble Sort, Quick Sort, Merge Sort)
- User management system for adding, retrieving, and deleting users
- Simple and intuitive interface for visualizing sorting processes
- Documentation for easy understanding and usage

## Technologies Used
- **Flask**: A micro web framework for Python
- **Flask-RESTX**: An extension for Flask that simplifies building RESTful APIs
- **Flask-Migrate**: A tool for handling SQLAlchemy database migrations
- **SQLAlchemy**: An ORM for Python that facilitates database interaction
- **Python**: The programming language used for development

## Installation
To get started with the project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/algorithm-visualizer.git
   cd algorithm-visualizer

2. **Set up a virtual environment:**
    python -m venv venv

3. **Install dependencies:**
    pip install -r requirements.txt

4. **Run the application:**
    python app.py

5. **API Endpoints**
    Sort Resource
    POST /sort/<algorithm>
    User Resource
    GET /user/<int:user_id>
    POST /user
    DELETE /user/<int:user_id>



