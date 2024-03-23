from functools import wraps
from flask import request, jsonify

def validate_request(schema):
    """
    Decorator function to validate request data against a given schema.

    Args:
        schema (dict): A dictionary representing the schema for request validation.

    Returns:
        function: The decorated function.
    """
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check if request data matches the schema
            errors = []
            for field, validation_fn in schema.items():
                if field not in request.json:
                    errors.append(f"{field} is required")
                elif not validation_fn(request.json[field]):
                    errors.append(f"Invalid {field} value")

            # If there are validation errors, return a 401 Unprocessed content
            if errors:
                return jsonify({'errors': errors}), 401

            # If validation passes, call the original function
            return func(*args, **kwargs)

        return wrapper
    return decorator