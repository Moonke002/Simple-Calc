# name: brayden
# date: 2025-03-28
# purpose: this program is a simple calculator that allows the user to add, subtract, multiply, and divide two numbers.  it is a web application that uses flask to create a simple calculator.

from flask import Flask, render_template, request, jsonify

# initialize flask application
app = Flask(__name__)

# route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# route for handling calculations
@app.route('/calculate', methods=['POST'])
def calculate():
    # get data from request
    data = request.get_json()
    num1 = float(data.get('num1', 0))
    num2 = float(data.get('num2', 0))
    operation = data.get('operation', '')
    
    # perform calculation based on operation
    result = 0
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            return jsonify({'error': 'Cannot divide by zero'}), 400
    
    return jsonify({'result': result})

# run the application
if __name__ == '__main__':
    app.run(debug=True) 