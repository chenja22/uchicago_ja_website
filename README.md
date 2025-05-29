# UChicago JA Website

## Overview
A clean, responsive website for the UChicago Junior Achievement chapter built with Flask.

## Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/username/uchicago_ja_website.git
   cd uchicago_ja_website

2. Create a virtual environment and install dependencies:
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

3. Run the application:
    export FLASK_APP=app.py
    flask run

4. Open your browser at http://127.0.0.1:5000

Project Structure
- app.py – application entry point with route definitions
- templates/ – Jinja2 HTML templates
- static/ – CSS, JS, and image assets