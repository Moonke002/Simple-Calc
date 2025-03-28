# Simple Calculator

A web-based calculator application that performs basic arithmetic operations with a clean, modern interface.

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Start the Flask backend:
```bash
python app.py
```

3. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Enter the first number in the "First Number" input field
2. Enter the second number in the "Second Number" input field
3. Click one of the operation buttons:
   - Add (+)
   - Subtract (-)
   - Multiply (×)
   - Divide (÷)
4. View the result displayed below the buttons

## Technical Details

- Backend: Python Flask
- Frontend: HTML, CSS, JavaScript
- API Endpoints:
  - GET /: Serve the calculator interface
  - POST /calculate: Perform arithmetic operations
    - Request body: { "num1": number, "num2": number, "operation": "add|subtract|multiply|divide" }
    - Response: { "result": number } or { "error": "message" }

## Features

- Clean, responsive user interface
- Support for decimal numbers
- Error handling for division by zero
- Real-time calculation results
- Mobile-friendly design

## Note

This is a simple calculator application demonstrating basic web development with Flask. 