Add `validate_email(email: str) -> bool` utility that performs a conservative
regular-expression based validation of email addresses.

Why:
- Needed by many parts of the app to do a quick sanity-check before sending emails.
- Avoids duplicate implementations across services.

What changed:
- Added `email_utils.py` with `validate_email`.
- Added tests in `test_email_utils.py` (pytest).

Tests:
- Unit tests cover valid emails, invalid emails, whitespace trimming, non-string input.

Notes:
- This is not a full RFC 5322 validator; it's intended to be fast and practical.
- If stricter validation is required later, we could plug in a well-tested library.
