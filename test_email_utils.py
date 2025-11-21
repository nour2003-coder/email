# test_email_utils.py
import pytest
from email_utils import validate_email

@pytest.mark.parametrize(
    "email,expected",
    [
        ("user@example.com", True),
        ("USER@EXAMPLE.COM", True),
        ("first.last@sub.domain.co", True),
        ("name+tag@domain.com", True),
        ("user@localhost", False),          # no TLD
        ("user@.com", False),
        ("@example.com", False),
        ("plainaddress", False),
        ("", False),
        (None, False),
        (" user@example.com ", True),       # leading/trailing whitespace OK
        ("user@domain.c", False),           # TLD too short
        ("user@domain.toolongtld", True),   # allow long TLDs
        ("user..name@example.com", False),  # double dot in local-part
        (".user@example.com", False),       # local-part starts with dot
    ],
)
def test_validate_email(email, expected):
    assert validate_email(email) is expected
