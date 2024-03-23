from app import app
from flask import url_for, request, jsonify
from app.decorators import validate_request
from app.validators import email_validator, password_validator

@app.route('/')
def index():
    index_url = url_for('index')
    return f'Hello, World! Visit the index page <a href="{index_url}">here</a>.'

@app.post('/login')
@validate_request({
    'email': [str, email_validator],
    'password': [str, password_validator],
})
def login_post():
    data = request.json
    
    # Start your route logic here
    
    response_data = {
        'message': 'Login data validated successfully', 
        'data': data,
    }
    
    # End your route logic here
    
    response = jsonify(response_data)
    
    response.status_code = 201
    
    return response

@app.post('/register')
@validate_request({
    'full_name': str,
    'email': [str, email_validator],
    'password': [str, password_validator],
})
def register_post():
    data = request.json
    
    # Start your route logic here
    
    response_data = {
        'message': 'Registration data validated successfully', 
        'data': data,
    }
    
    # End your route logic here
    
    response = jsonify(response_data)
    
    response.status_code = 201
    
    return response