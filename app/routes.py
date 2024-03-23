from app import app
from flask import url_for, request, jsonify
from app.validators import validate_request

@app.route('/')
def index():
    index_url = url_for('index')
    return f'Hello, World! Visit the index page <a href="{index_url}">here</a>.'

@app.post('/login')
@validate_request({
    'email': str,
    'password': str
})
def login_post():
    
    data = request.json
    # Your route logic here
    return jsonify({
        'message': 'Request data validated successfully', 
        'data': data,
    })

@app.post('/register')
def login_post():
    return 'register api request'