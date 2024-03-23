from functools import wraps
from flask import request, jsonify
from app.helpers import unslug

def validate_request(rules):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            errors = {}
            
            for field, validators in rules.items():

                field_value = request.json.get(field, None)
                field_name = field
                field_attribute = field.replace('_', ' ')

                if isinstance(validators, list):  # Check if validator is a list
                    for validator_fn in validators:
                        if callable(validator_fn):
                            result = validator_fn(field_value, field_name, field_attribute)
                            if result:
                                
                                if result.get('ignore_other_rules') is True:
                                    errors.pop(field, [])
                                    break
                                 
                                errors.setdefault(field, []).append({"code": result['code'], "message": result['error']})
                                
                else:
                    validator_fn = validators
                    if callable(validator_fn):  # If it's a single function
                        result = validator_fn(field_value, field_name, field_attribute)
                        if result:
                        
                            if result.get('ignore_other_rules') is True:
                                errors.pop(field, [])
                                
                            errors.setdefault(field, []).append({"code": result['code'], "message": result['error']})

            if errors:
                return errors, 422

            return func(*args, **kwargs)
        return wrapper
    return decorator
