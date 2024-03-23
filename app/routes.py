from app import app
from flask import url_for, request, jsonify
from app.decorators import validate_request
from app.validators import email_validator, password_validator, required, string, full_name_validator, sometimes

@app.route('/')
def index():
    index_url = url_for('index')
    return f'Hello, World! Visit the index page <a href="{index_url}">here</a>.'

@app.post('/login')
@validate_request({
    'email': [required, email_validator],
    'password': [required, password_validator],
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
    'full_name': [required, full_name_validator],
    'email': [required, email_validator],
    'password': [required, password_validator],
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

@app.get('/profile')
def profile_get():
    
    # Start your route logic here
    
    response_data = {
        'message': 'Current user profile data', 
        'data': {},
    }
    
    # End your route logic here
    
    response = jsonify(response_data)
    
    response.status_code = 200
    
    return response

@app.put('/profile')
@validate_request({
    'full_name': [sometimes, full_name_validator],
    'email': [sometimes, email_validator],
    'password': [sometimes, password_validator],
})
def profile_put():
    data = request.json
    
    # Start your route logic here
    
    response_data = {
        'message': 'Current user data updated successfull', 
        'data': data,
    }
    
    # End your route logic here
    
    response = jsonify(response_data)
    
    response.status_code = 201
    
    return response