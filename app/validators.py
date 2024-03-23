from flask import request
from email_validator import validate_email, EmailNotValidError
from password_strength import PasswordPolicy, PasswordStats

def required(value: any, name: str, attribute: str) -> dict:
    """Check if a value is present in the request JSON or not.

    Args:
        value (any): The value to check.
        name (str): The name of the field.
        attribute (str): The name of the field in human readable format.

    Returns:
        dict: A dictionary containing error information if the value is missing,
              otherwise returns None.
    """
    if name not in request.json or value is None:
        return {'code': 'required', 'error': f'{attribute} is required'}

def nullable(value: any, name: str, attribute: str) -> dict:

    if value is None:
        return {'ignore_other_rules': True}

def sometimes(value: any, name: str, attribute: str) -> dict:

    if name not in request.json or value is None:
        return {'ignore_other_rules': True}
    
def full_name_validator(value: str, name: str, attribute: str) -> dict:
    """Validate the full name.

    Args:
        value (str): The full name to validate.
        name (str): The name of the field.
        attribute (str): The name of the field in human readable format.

    Returns:
        dict: A dictionary containing error information if the full name is invalid,
              otherwise returns None.
    """
    if not isinstance(value, str):
        return {'code': 'invalid_data_type', 'error': f'{attribute} must be a string'}
    
    if name not in request.json or value is None or len(value) < 8:
        return {'code': 'invalid_full_name_length', 'error': f'{attribute} must be at least 8 characters long'}

def email_validator(value: str, name: str, attribute: str) -> dict:
    """Validate the email address format.

    Args:
        value (str): The email address to validate.
        name (str): The name of the field.
        attribute (str): The name of the field in human readable format.

    Returns:
        dict: A dictionary containing error information if the email format is invalid,
              otherwise returns None.
    """
    if '@' not in value:
        return {'code': 'invalid_email', 'error': f'invalid {attribute} format'}

def password_validator(value: str, name: str, attribute: str) -> dict:
    """Validate the password strength.

    Args:
        value (str): The password to validate.
        name (str): The name of the field.
        attribute (str): The name of the field in human readable format.

    Returns:
        dict: A dictionary containing error information if the password is weak,
              otherwise returns None.
    """
    if name not in request.json or value is None or len(value) < 8:
        return {'code': 'weak_password', 'error': f'{attribute} must be at least 8 characters long'}

def string(value: str, name: str, attribute: str) -> dict:
    """Validate if the value is a string.

    Args:
        value (str): The value to validate.
        name (str): The name of the field.
        attribute (str): The name of the field in human readable format.

    Returns:
        dict: A dictionary containing error information if the value is not a string,
              otherwise returns None.
    """
    if not isinstance(value, str):
        return {'code': 'invalid_data_type', 'error': f'{attribute} must be a string'}
