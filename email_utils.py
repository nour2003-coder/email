# email_utils.py
"""
Simple email validation helper.

This file contains a small utility function validate_email that
returns True for valid-looking emails and False otherwise.
"""

import re
from typing import Pattern

# basic RFC-like local@domain pattern (not fully RFC 5322 compliant but practical)
_EMAIL_REGEX: Pattern = re.compile(
    r"^[a-z0-9]+[a-z0-9._%+-]*@[a-z0-9.-]+\.[a-z]{2,}$",
    flags=re.IGNORECASE,
)


def validate_email(email: str) -> bool:
    """
    Return True if `email` appears to be a valid email address, False otherwise.

    The function performs a conservative pattern match (not full RFC compliance).
    """
    if not isinstance(email, str):
        return False
    email = email.strip()
    if not email:
        return False
    return bool(_EMAIL_REGEX.match(email))
