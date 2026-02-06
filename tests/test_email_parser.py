from backend.gmail_tools import read_email

def test_read_email():
    email = read_email()
    assert "subject" in email
    assert "body" in email
