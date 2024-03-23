from flask import request
from email_validator import validate_email, EmailNotValidError
from password_strength import PasswordPolicy, PasswordStats

def required(value, name):
    if value not in request.json:
        return {"code": "required", "error": f"{name} is required"}

def full_name_validator(value, name):
    if not isinstance(value, str):
        return {'code': 'invalid_data_type', 'error': f"{name} must be a string"}
    
    if len(value) < 8:
        return {'code': 'invalid_full_name_lenght', 'error': f"{name} must be at least 8 characters long"}

def email_validator(value, name):
    if not '@' in value:
        return {'code': 'invalid_email', 'error': f"invalid {name} format"}

def password_validator(value, name):
    if len(value) < 8:
        return {'code': 'weak_password', 'error': f"{name} must be at least 8 characters long"}

def string(value, name):
    if not isinstance(value, str):
        return {'code': 'invalid_data_type', 'error': f"{name} must be a string"}