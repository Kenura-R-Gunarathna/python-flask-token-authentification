from functools import wraps
from flask import request, jsonify
from app.helpers import unslug

def validate_request(schema):
    """
    Decorator function to validate request data against a given schema.

    Args:
        schema (dict): A dictionary representing the schema for request validation.
                      Each value in the schema can be either a single validator function
                      or a list of validator functions.

    Returns:
        function: The decorated function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check if request data matches the schema
            errors = {}
            for field, validators in schema.items():
                field_name = unslug(field, "_")
                
                # Convert single validator to a list for consistency
                if not isinstance(validators, list):
                    validators = [validators]
                
                # Apply each validator to the field
                for validator_fn in validators:
                    if field not in request.json:
                        errors.setdefault(field, []).append({"code": "required", "message": f"{field_name} is required"})
                    elif not validator_fn(request.json[field]):
                        errors.setdefault(field, []).append({"code": "invalid", "message": f"Invalid {field_name} value"})

            # If there are validation errors, return a 422 Unprocessable Entity
            if errors:
                return jsonify({'errors': errors}), 422

            # If validation passes, call the original function
            return func(*args, **kwargs)

        return wrapper
    return decorator
