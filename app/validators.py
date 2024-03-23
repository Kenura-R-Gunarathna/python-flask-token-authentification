from email_validator import validate_email, EmailNotValidError
from password_strength import PasswordPolicy, PasswordStats

def email_validator(email):
    """
    Validate an email address using the email-validator library.

    Args:
        email (str): Email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

def password_validator(password):
    """
    Validate a password strength using the password-strength library.

    Args:
        password (str): Password to validate.

    Returns:
        bool: True if the password meets the defined criteria, False otherwise.
    """
    policy = PasswordPolicy.from_names(
        length=8,  # Minimum length
        uppercase=1,  # Require at least one uppercase letter
        numbers=1,  # Require at least one digit
        special=1,  # Require at least one special character
    )
    stats = PasswordStats(password)
    return policy.test(stats)
