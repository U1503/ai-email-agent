import os
import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def get_service():
    creds = None

    if os.path.exists('backend/token.json'):
        creds = Credentials.from_authorized_user_file('backend/token.json', SCOPES)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'backend/credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

        with open('backend/token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    return service


def read_email():
    service = get_service()

    results = service.users().messages().list(
        userId='me',
        labelIds=['INBOX'],
        maxResults=1
    ).execute()

    messages = results.get('messages', [])

    if not messages:
        return {"subject": "No Emails", "body": "Inbox empty"}

    msg = service.users().messages().get(
        userId='me',
        id=messages[0]['id']
    ).execute()

    payload = msg['payload']
    headers = payload['headers']

    subject = ""
    for header in headers:
        if header['name'] == 'Subject':
            subject = header['value']

    body = ""

    if 'parts' in payload:
        body_data = payload['parts'][0]['body'].get('data')
    else:
        body_data = payload['body'].get('data')

    if body_data:
        body = base64.urlsafe_b64decode(body_data).decode()

    return {"subject": subject, "body": body}


def send_email(to, subject, body):
    service = get_service()

    message = MIMEText(body)
    message['to'] = to
    message['subject'] = subject

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

    service.users().messages().send(
        userId='me',
        body={'raw': raw}
    ).execute()

    return "Email sent successfully"
